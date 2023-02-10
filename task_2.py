def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(int(i))
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return set(primfac)

def get_int():
    while True:
        try:
            num = int(input("Enter number: "))
            return num
        except ValueError:
            print("Incorrect number!")
            continue

print(*primfacs(get_int()))