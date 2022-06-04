# Простые числа 2 3 5 7 11 13 17 19 23 29
#13195
#5 2639
#5 7 377
#5 7 13 29


number = int(input("Введите число:"))

temp_del = 2
temp_number = number
simples = []

while temp_del < temp_number: # 5 13195

    is_simple = True

    for simple in simples: # [2, 3]
        if temp_del % simple == 0:
            print(temp_del)
            is_simple = False # 5 не дойдёт

    if is_simple == True: # 5 не дошла ^
        simples.append(temp_del) # Добавляем простое число в список [2, 3, 5]
        while temp_number % temp_del == 0 and temp_number != temp_del:
            #print(temp_del)
            temp_number = int(temp_number / temp_del) # 13195 / 5 = 2639
            #print(temp_number)
    temp_del+=1

print("Наибольший простой делитель:", temp_number)

