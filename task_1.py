import math
def calc_pi(d):
    pi = 1
    i = 1
    z = 1
    acc = 0
    while d < 1:
        pi -= z/((2*i+1)*3**i)
        z = -1*z
        d*=10
        i+=1
        acc+=1
    #return pi
    pi = pi * math.sqrt(12)
    return round(pi, acc)

def get_float():
    while True:
        try:
            num = float(input("Enter pi num acc: "))
            return num
        except ValueError:
            print("Incorrect number!")

print(calc_pi(get_float()))