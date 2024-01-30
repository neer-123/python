#Write a function using a generator to print the numbers which can be divisible by 5 and 7 between 0 and given number n  in comma separated form. 
	#E.g - given number = 100 . output = 0,35,70



def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

def print_numbers(n):
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))


print_numbers(100)
