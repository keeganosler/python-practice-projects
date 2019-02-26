#checks if a given number has a trailing zero and if it does, removes it

def no_zeros(num):
    last_digit = num%10
    if(last_digit == 0):
        num = num//10
        print(num)
    else:
        print(num)

no_zeros(1234)
no_zeros(1230)

