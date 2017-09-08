# the variadic example

def sum( *nums):
    print(nums,end=" ")
    total = 0
    for num in nums:
        total += num

    print(total)

def main():

    sum(1, 2)
    sum(1, 2, 3)

    nums = (1, 2, 3, 4)
    sum(*nums)

main()
