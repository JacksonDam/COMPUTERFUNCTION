def COMPUTERFUNCTION(a, b):
    return int(bin(a ^ b), 2)

splitInput = input("Enter two numbers separated by a space (x y): \n").split()
print(COMPUTERFUNCTION(int(splitInput[0]), int(splitInput[1])))