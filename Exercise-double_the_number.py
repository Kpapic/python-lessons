def double(num):
    return num * 2

interations = int(input("How many numbers you wont to double?"))

for i in range(interations):
    num = int(input("Enter the number: "))
    result = double(num)
    print(f"The double of {num} is {result}")