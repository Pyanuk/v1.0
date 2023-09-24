import math

def calculator():
    print("Выберите операцию:")
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
    print("11. Выход")

    operation = input("Введите номер операции: ")
    if operation == "11":
        print("Бай бай")
        return

    if operation == '1':
        number1 = float(input("Введите первое число: "))
        number2 = float(input("Введите второе число: "))
        result = number1 + number2
        print("Результат: ", result)

    elif operation == '2':
        number1 = float(input("Введите первое число: "))
        number2 = float(input("Введите второе число: "))
        result = number1 - number2
        print("Результат: ", result)

    elif operation == '3':
        number1 = float(input("Введите первое число: "))
        number2 = float(input("Введите второе число: "))
        result = number1 * number2
        print("Результат: ", result)

    elif operation == '4':
        number1 = float(input("Введите первое число: "))
        number2 = float(input("Введите второе число: "))
        if number2 == 0:
            print("Ошибка: деление на 0 недопустимо")
        else:
            result = number1 / number2
            print("Результат: ", result)

    elif operation == '5':
        number = float(input("Введите число: "))
        power = float(input("Введите степень: "))
        result = math.pow(number, power)
        print("Результат: ", result)

    elif operation == '6':
        number = float(input("Введите число: "))
        if number < 0:
            print("Ошибка: квадратный корень из отрицательного числа недопустим")
        else:
            result = math.sqrt(number)
            print("Результат: ", result)

    elif operation == '7':
        number = int(input("Введите число: "))
        if number < 0:
            print("Ошибка: факториал отрицательного числа недопустим")
        else:
            result = math.factorial(number)
            print("Результат: ", result)

    elif operation == '8':
        number = float(input("Введите число: "))
        result = math.sin(math.radians(number))
        print("Результат: ", result)

    elif operation == '9':
        number = float(input("Введите число: "))
        result = math.cos(math.radians(number))
        print("Результат: ", result)

    elif operation == '10':
        number = float(input("Введите число: "))
        result = math.tan(math.radians(number))
        print("Результат: ", result)

    else:
        print("Ошибка: некорректный номер операции")

    print("\n")
    calculator()


calculator()
