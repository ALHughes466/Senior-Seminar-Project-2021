import time
import statistics
import math


# convert a number into 32-bit unsigned int
def int_32(number):
    return int(0xFFFFFFFF & number)


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
    i = 0
    # x = 0
    # w = 0
    # x and w are initialized as non-zero so there will be randomness in the first iteration
    w = x = int(time.time())
    x = int_32(x)
    s = 0x9f32e1cbc5e1374b
    already_seen = set()

    while True:
        # validate input
        user_input2 = input("Enter initial seed or press enter to generate seed:\n")
        if user_input2 == "":
            break
        try:
            w = x = int(user_input2)
            x = int_32(x)
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            user_input = int(input("How many numbers do you want to generate?\n"))
            break
        except ValueError:
            print("Invalid input.")

    start_time = time.time()
    while i < user_input:
        # check if a seed has already been seen
        if x in already_seen:
            print(f"Generator looped after {i} numbers.")
            break
        # add to list of values
        already_seen.add(x)
        # increment counter
        i += 1
        # generator
        x *= x
        w += s
        x += w
        # x needs to be an unsigned 32 bit integer to shift the bits
        x = int_32(x)
        # shift bits
        x = (x >> 32) | (x << 32)
        print(x)
    # add last generated value to seen list
    already_seen.add(x)
    end_time = time.time()
    calculate(start_time, end_time, already_seen, i)
    print(f"Generated {i} numbers.")


print("Middle Square Weyl Sequence Generator")
main()
