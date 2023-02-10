import random
def write_polynomial_to_file(k):
    res = f""
    for i in range(k):
        koeff = random.randint(0,100)
        if koeff:
            res += f"{koeff}*x^{k-i} + "
    res += f"{random.randint(1,100)} = 0"
    my_file = open("result.txt","w+")
    my_file.write(res)
    my_file.close()

def get_int():
    while True:
        try:
            num = int(input("Enter polynom power: "))
            return num
        except ValueError:
            print("Incorrect number!")
            continue

write_polynomial_to_file(get_int())

