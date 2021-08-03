sum = 0

print("\"Warning\"","\n","\bIf you want end the program and see the sum , pls enter 'exit'")

while True :
    x = input("pls enter a number: ")
    
    if x == 'exit':
        break

    else:
        x = int(x)
        sum += x

print("Sum is:",sum)