decimal = 10
result = ""
while decimal > 0:
    decimal = decimal//2
    reminder = decimal %2

    result = str(reminder) + result
print(result)
