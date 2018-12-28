#/usr/bin/env python3
import random 

N_SAMPLES = 1000


# #########################################################################
# Naive - pure python implementation
def single_random_sample():
    return [random.uniform(0., 1.), random.uniform(0., 1.)] 

def generate_samples(n_samples):
    return [single_random_sample() for i in range(n_samples)]

def check_sample(sample):
    # This function returns true if the sample is inside a circle of radius 1, centered on (0,0)
    return (sample[0]*sample[0] + sample[1]*sample[1]) < 1.

def run_naive():
    samples = generate_samples(N_SAMPLES)
    n_inside = 0

    for sample in samples:
        if check_sample(sample):
            n_inside += 1

    pi_estimate = (4. * n_inside) / N_SAMPLES
    print("Our estimate of Pi is {}".format(pi_estimate))


run_naive()