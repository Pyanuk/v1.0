import math


def calculator():
    print("Калькулятор")
    print("Выберите номер операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")

    operation = input("Введите номер операции: ")

    if operation in ['1', '2', '3', '4']:
        pervoyechislo= float(input("Первое число:"))
        vtoroyechislo= float(input("Второе число:"))

        if operation == '1':
            result = pervoyechislo + vtoroyechislo
            print("Результат:", result)
        elif operation == '2':
            result = pervoyechislo - vtoroyechislo
            print("Результат:",result)
        elif operation == '3':
            result = pervoyechislo * vtoroyechislo
            print("Результат:",result)
        elif operation == '4':
            if vtoroyechislo == 0:
                print("Результат:делить на ноль нельзя")
            else:
                result = pervoyechislo / vtoroyechislo
                print("Результат:",result)
    elif operation == '5':
        pervoyechislo= float(input("Введите число: "))
        ctepen = float(input("Введите степень: "))
        result = pervoyechislo ** stepen
        print("Результат: ", result)
    elif operation == '6':
        number = float(input("Введите число для извлечения квадратного корня: "))
        if number < 0:
            print("Ошибка: отрицательное число")
        else:
            result = math.sqrt(number)
            print("Результат: ", result)
    elif operation == '7':
        number = int(input("Введите число для вычисления факториала: "))
        result = 1
        if number < 0:
            print("Ошибка: отрицательное число")
        else:
            for i in range(1, number + 1):
                result *= i
            print("Результат: ", result)
    elif operation in ['8', '9', '10']:
        angle = math.radians(float(input("Введите угол в градусах: ")))
        if operation == '8':
            result = math.sin(angle)
            print("Результат: ", result)
        elif operation == '9':
            result = math.cos(angle)
            print("Результат: ", result)
        elif operation == '10':
            result = math.tan(angle)
            print("Результат: ", result)
    else:
        print("Ошибка: некорректный номер операции")


calculator()