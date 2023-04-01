def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num_tests = int(input("Enter the number of test cases: "))
for test_case in range(num_tests):
    num = int(input("Enter a number: "))

    # extract digits from num and check if they're prime
    digit_list = []
    while num != 0:
        digit = num % 10
        if is_prime(digit):
            digit_list.append(digit)
        num //= 10
    
    # print the list of prime digits
    if digit_list:
        print(f"Prime digits in {test_case+1}th number: {digit_list}")
    else:
        print(f"No prime digits in {test_case+1}th number")
