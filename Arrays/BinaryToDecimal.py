def binToDecMethod1(binary):
    decimal = 0
    i = 0
    while binary != 0:
        rem =  binary % 10
        binary = binary // 10
        decimal = decimal + (rem * pow(2, i) )
        i += 1
    print("Decimal by method 1:", decimal)

def binToDecMethod2(binary):

    decimal = 0
    binary = str(binary)
    for bit in binary:
        decimal = decimal*2 + int(bit)
    print("Decimal by method 2:", decimal)


binary = 100100
binToDecMethod1(binary)
binToDecMethod2(binary)
