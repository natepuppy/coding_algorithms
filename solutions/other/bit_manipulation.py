# Counting Bits
def countBits(n):
    count = 0
    while n:
        # This WILL NOT WORK - This will just count how many bits it takes to reach the last one... ex: 1000 ---> 0100
        # if n >> 1 > 0:
        #     count += 1

        if n & 1:
            count += 1

        n = n >> 1

    return count

n = 13

print(countBits(n))

# built in ways:
print(n.bit_count())
# OR
print(bin(n).count('1'))
