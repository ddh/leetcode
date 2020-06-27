def generalizedGCD(num, arr):


    if num == 1:
        return arr[0]


    def gcd(num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        if num1 == num2:
            return num1
        if num1 > num2:
            num1,num2 = num2,num1

        return gcd(num2, num1 % num2)

    current_gcd = arr[0]
    pointer = 1
    while pointer < num:
        print(current_gcd)
        print(arr[pointer])
        current_gcd = gcd(current_gcd, arr[pointer])
        pointer += 1

    print(current_gcd)

    return current_gcd


generalizedGCD(5, [2,4,6,8,10])