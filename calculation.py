def add(num):
    value = 0
    for n in num:
        value = value + int(n)

    return value

def mul(num):
    value = 1
    for n in num:
        value = value * int(n)

    return value   

def div():
    dividend = input("Enter dividend: ")
    divisor = input("Enter divisor: ")
    quotient = int(dividend) / int(divisor)
    return quotient

def sub(numbers):
    value = int(numbers[0])
    
    for num in numbers[1:]:
        value = value - int(num)

    return value    

operation = input("Enter operation: ")

if operation != "div":
    value = input("Enter the numbers: ")
    operands = value.split(",")     
    

if operation == "add":
    result = add(operands)
    print(result)

elif operation == "mul":
    result = mul(operands)
    print(result)

elif operation == "div":
    result = div()
    print(result)    

if operation == "sub":
    result = sub(operands)
    print(result)

else: 
    print("operation not found")    

    


    