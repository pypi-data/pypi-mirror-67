#!/usr/bin/env python
# coding: utf-8


import numpy as np
from importlib import reload
from multiprocessing import Pool
from itertools import combinations, permutations
import logging
from sys import getsizeof
from scipy import stats, sparse
from tqdm import tqdm
import time
import istarmap



def delay_per_timepoint(vox, activ, t, delay_list, n_regions):
    '''
    Delay measurement routine for a particular timepoint:
    '''

    # Initializing delay measures as a sparse matrix for each "active" time point
    #delay_meas = sparse.lil_matrix((n_regions, n_regions), dtype = float)
    delay_meas = sparse.lil_matrix((n_regions, n_regions), dtype = np.uint16)
    # Store index of previously (act) and newly (vox) activated regions 
    act_idx = np.where(activ != 0)[0]
    vox_idx = np.where(vox != 0)[0]
    
    # Computation of time delay between
    if any(activ):
        for vox_id in vox_idx:
            delay_meas[act_idx, vox_id] = (t + 1 - activ[act_idx])
    
    delay_list.append(delay_meas)
    
    # Update activation list and times
    activ[np.where(vox != 0)] = t + 1
    
    return

def par_delay(vox_1, vox_2):
    '''
    Parallel implementation of Delay Measurement Algorithm:
    '''
    
    timepoints, activ = np.where(np.array([vox_1, vox_2]).T != 0)
    
    n_act = len(activ)
    
    my_del = np.full((2, n_act - 1), np.nan)
    
    simul = False
    prev_act = np.full((2), np.nan)
    
    for i in range(0, n_act, 1):
        
        my_del[1 - activ[i], i - 1] = timepoints[i] - prev_act[1 - activ[i]]
        
        if simul:
            prev_act[activ[i - 1]] = timepoints[i - 1]
            
        simul = ((i + 1 < n_act) and (timepoints[i] == timepoints[i + 1]))
        
        if not simul:
            prev_act[activ[i]] = timepoints[i]
    
    results = np.empty((2, 2))
    for i, row in enumerate(my_del):
        no_nan = row[~np.isnan(row)]
        results[:, i] = no_nan.mean(), no_nan.std()
    
    return results

def delay_measure(signal, return_meas = False, parallel = True, progress = False, **kwargs):
    '''
    Main delay framework algorithm:
    '''
    #reload(logging)
    #logging.basicConfig(filename = 'delay_perf.log', level = logging.INFO, filemode = 'w')
    
    n_regions = len(signal)
    n_timepoints = len(signal[0])

    print('Working with {} regions and {} timepoints'.format(n_regions, n_timepoints))

    delay_mean = np.full((n_regions, n_regions), np.nan)
    delay_std = np.full_like(delay_mean, np.nan)

    tb_meas = time.perf_counter()
    
    if parallel:
        print('Using Parallel Implementaion')
        indices = np.transpose(np.triu_indices_from(delay_mean, 1))

        print('Measuring delays...')
        #logging.info('Measuring delays...')

        n_tasks = sum(1 for _ in combinations(signal, 2))
        #delay_measures = []

        with Pool(processes = None) as pool:
            if progress:
                for idx, pool_res in enumerate(tqdm(pool.istarmap(par_delay, combinations(signal, 2), **kwargs))):
                    for i, perm in enumerate(permutations(indices[idx])):
                        delay_mean[perm] = pool_res[0][i]
                        delay_std[perm] = pool_res[1][i]
            else:
                for idx, pool_res in enumerate(pool.istarmap(par_delay, combinations(signal, 2), **kwargs)):
                    for i, perm in enumerate(permutations(indices[idx])):
                        delay_mean[perm] = pool_res[0][i]
                        delay_std[perm] = pool_res[1][i]

                ## Old methods
                #delay_measures = pool.starmap(par_delay, combinations(signal, 2), **kwargs)
                #delay_measures = list(pool.istarmap(par_delay, combinations(signal, 2), **kwargs))

            ta_meas = time.perf_counter()
            print('Measurement done after {}s.'.format(ta_meas - tb_meas))
            #logging.info('Measure done in {}s.'.format(ta_meas - tb_meas))

    else:
        print('Using Straight Forward Implementaion')
        # Initialization of data vectors
        activ = np.zeros((n_regions))
        delay_list = []
        
        print('Measuring delays...')
        #logging.info('Measuring delays...')
        
        # Scanning through time
        for t, vox in enumerate(signal.T):
            
            # Progression Verbose
            #if ((t+1) % np.ceil(n_timepoints/10) == 0):
            #    print('––', t+1, 'out of', n_timepoints)
            
            # Compute delay and update activation list iif at least one region is active
            if any(vox):
                delay_per_timepoint(vox, activ, t, delay_list, n_regions)
        
        ta_meas = time.perf_counter()
        print('Measurement done after {}s.'.format(ta_meas - tb_meas))
        #logging.info('Measure done in {}s.'.format(ta_meas - tb_meas))
        
        n_active = len(delay_list)
        
        print('Computing mean and STD ({} out of {} time points)...'.format(n_active, n_timepoints))
        #logging.info('Computing mean and STD ({} out of {} time points)...'.format(n_active, n_timepoints))
        
        for row_id in range(n_regions):
            tmp = np.empty((n_regions, n_active))
            
            for t in range(n_active):
                tmp[:, t] = delay_list[t].getrow(row_id).toarray()
                
            tmp[tmp == 0] = np.nan
            
            delay_mean[row_id] = np.nanmean(tmp, axis = 1)
            delay_std[row_id] = np.nanstd(tmp, axis = 1)

            delay_mean[row_id, row_id] = np.nan
            delay_std[row_id, row_id] = np.nan
        
        ta_comp = time.perf_counter()
        print('Computation done after {}s.'.format(ta_comp - ta_meas))
        #logging.info('Computation done in {}s.'.format(ta_comp - ta_meas))
    #print('–#– Delay Measurement Succeeded –#–')
    #logging.info('–#– Delay Measurement Succeeded –#–')
    
    if return_meas:
        return delay_list, delay_mean, delay_std
    else:
        return delay_mean, delay_std


def piecewise_activity(n_timesteps = 1000, trans_prob = 1e-3, trans_amp = 5, noise = 0):
    time_course = np.empty((n_timesteps))
    innovation = np.zeros_like(time_course)
    time_course[0] = np.random.normal(0, 5)
    last_trans = 0
    # Storing progression of numbers of draw (in binomial)
    n_draws = []

    for t in np.arange(1, n_timesteps, 1):
        if np.random.binomial(t - last_trans, trans_prob):
            # Computation of transition amplitude
            transition = np.random.normal(0, trans_amp)
            
            # Storthe progression of n_draws
            n_draws.extend(np.arange(t-last_trans))
            
            time_course[t] = transition
            last_trans = t
            
            # Randomization of transition probablity
            trans_prob = abs(np.random.normal(trans_prob, trans_prob/10))
            
            innovation[t] = transition - time_course[t-1]
        else:
            time_course[t] = time_course[t - 1]
            
    n_draws.extend(np.arange(t - last_trans))
    
    if noise:
        time_course += np.random.normal(np.zeros_like(time_course), noise)
        innovation += np.random.normal(np.zeros_like(time_course), noise)
    
    return time_course, innovation, n_draws

sig, inno, n_draws = piecewise_activity(500, trans_prob = 1e-3, noise = .2)


def gen_follower(seed, delay, activ_prob = 100, rand_delay = 1, noise = 0):
    
    follower = np.zeros_like(seed)
    
    # Computation of random delay
    peaks = np.where(np.abs(stats.zscore(seed)) > 1.5)[0]
    shift = peaks + delay + np.random.normal(np.zeros_like(peaks), rand_delay)
    shift = np.ceil(shift).astype(int)
    
    # Discard activity at time larger than n_timepoints
    shift = shift[shift < len(seed)]
    
    # Assign a random value (from the value of the activity of the seed) to the followers
    follower[shift] = np.random.choice(seed[peaks], len(shift))
    
    # Randomly set activity of a follower to 0 with probability "activ_prob"
    n_rand_act = np.percentile(np.arange(len(shift)), 100 - activ_prob,
                               interpolation = 'nearest')
    n_rand_act = np.random.binomial(len(shift), 1 - activ_prob/100)
    rand_discard = np.random.choice(shift, n_rand_act)
    
    follower[rand_discard] = 0
    
    # Add random activity (regardless of the seed activity)
    unactiv_id = np.where(follower == 0)[0]
    rand_act = np.random.choice(unactiv_id, n_rand_act)

    follower[rand_act] = np.random.choice(seed[peaks], n_rand_act)
    
    added_noise = np.random.normal(np.zeros_like(seed), noise)
    follower += added_noise
    
    return follower

def simulate_activation(n_regions = 20, n_seeds = 2, n_followers = 2,
                        n_timepoints = 400, delay = 10, activ_proba = [0, 100],
                        piecewise = False, **kwargs):
    # Initialization of time course
    time_course = np.empty((n_regions, n_timepoints))

    # Random group allocation of region id
    non_random_id = np.random.choice(n_regions, n_seeds + n_followers, replace = False)
    
    seeds_id = non_random_id[:n_seeds]
    followers_id = non_random_id[n_seeds:n_seeds + n_followers]
    
    # Use of innovation signals from piecewise constant voxel activity
    if piecewise:
        for i in np.arange(n_regions):
            _, time_course[i], _ = piecewise_activity(n_timepoints, **kwargs)
    # Use of random, sparse innovation signals
    else:
        # Initialization of time course with random activities
        time_course = np.random.normal(np.zeros((n_regions, n_timepoints)), 1)

        # Generation of random activity (all regions)
        for region in time_course:
            thresh = np.percentile(region, 100 - activ_proba[0])
            region[abs(region) < thresh] = 0
    
    # Generation of followers states (random choice of seed)
    seed_choice = []
    for i in range(n_followers):
        seed_choice.append(np.random.choice(n_seeds))
        chosen = time_course[seeds_id[seed_choice[i]]]
        # Generation of follower
        time_course[followers_id[i]] = gen_follower(chosen, delay, activ_proba[1], **kwargs)
    
    return time_course, seeds_id, followers_id, seed_choice