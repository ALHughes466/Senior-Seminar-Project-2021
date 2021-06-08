import time
import statistics
import math


def lcg(mod, a, c, seed, length):
    # Linear congruential generator
    # using Microsoft C++'s modulus m, multiplier a, increment c
    i = 0
    # we want to measure how many times the period loops
    loops = 0
    original_seed = seed
    while True:
        seed = (a * seed + c) % mod
        i += 1
        yield seed
        if original_seed == seed:
            loops += 1
        if i >= length:     # reached the inputted amount of numbers to generate
            break

    # print how many values were generated
    if length == 1:
        print("Generated 1 value.")
    else:
        print("Generated " + str(i) + " values.")
    # check if algorithm period was reached (values generated > 2^32)
    if loops > 1:
        print("Period was reached " + str(loops) + " times.")
    elif loops > 0:
        print("Period was reached " + str(loops) + " time.")
    else:
        print("Period was not reached.")


def calculate(start, end, values, length):
    # calculate runtime
    runtime = end - start
    # calculate variance of numbers
    # variance = statistics.pvariance(values)
    avg_time = runtime/length
    # print("Variance: %s" % variance)
    # square root of variance is standard deviation
    # stdev is the metric used for the distribution of generated numbers
    # larger spread = better algorithm
    print("Standard deviation: %s" % statistics.pstdev(values))
    # runtime is the metric for algorithm speed
    print("Runtime: %s seconds" % str(runtime))
    print(f"Average runtime per number generated: {avg_time} seconds")


def main():
    # initialize mod, a, and c using the values used by Microsoft C++ random method
    mod = 2**32     # period should be equal to the modulus
    a = 214013
    c = 2531011
    # initialize list for storing values
    values = []
    # use time as seed or user seed

    while True:
        u_input1 = (input("Do you want to input your own seed? Y/n \n").lower())
        if u_input1 == "y" or u_input1 == "n":
            break
        else:
            print("Incorrect entry.")

    # check input
    if u_input1 == "n":
        # set seed to seconds since epoch
        print("Using seed " + str(int(time.time())))
        seed = int(time.time())
        while True:
            # validate input
            try:
                length = int(input("How many numbers do you want to output?\n"))
                break
            except ValueError:
                print("Invalid length.")
        # begin measuring time
        start_time = time.time()
        for num in (lcg(mod, a, c, seed, length)):
            print(num)
            values.append(num)
        # end measuring time
        end_time = time.time()
        calculate(start_time, end_time, values, length)

    else:
        while True:
            # validate input
            try:
                seed = int(input("Input numeric seed:\n"))
                break
            except ValueError:
                print("Invalid seed.")
        while True:
            try:
                length = int(input("How many numbers do you want to output?\n"))
                break
            except ValueError:
                print("Invalid length.")
        # begin measuring time
        start_time = time.time()
        for num in (lcg(mod, a, c, seed, length)):
            print(num)
            values.append(num)
        # end measuring time
        end_time = time.time()
        calculate(start_time, end_time, values, length)


print("Linear Congruential Generator")
main()
