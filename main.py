def decimalToBinary(num):
    if num > 3:
            decimalToBinary(num // 5)
    print(num % 5, end='')
        
number = int(input("Ievadiet jebkuru decimalo skaitli:"))
decimalToBinary(number)