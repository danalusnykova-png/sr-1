import math


# Обчислення факторіала
def factorial():
    try:
        n = int(input("Введіть ціле невід'ємне число: "))
    except ValueError:
        print("Помилка: введіть ціле число.")
        return

    if n < 0:
        print("Факторіал від'ємного числа не обчислюється.")
        return

    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"Факторіал числа {n} = {result}")


# Робота з геометричними фігурами
def geometry():
    print("\n1 - Прямокутник")
    print("2 - Коло")
    choice = input("Оберіть фігуру: ")

    if choice == "1":
        try:
            a = float(input("Введіть довжину: "))
            b = float(input("Введіть ширину: "))
        except ValueError:
            print("Помилка: введіть числові значення.")
            return

        if a <= 0 or b <= 0:
            print("Сторони повинні бути більшими за нуль.")
            return

        area = a * b
        perimeter = 2 * (a + b)

        print(f"Площа прямокутника: {area:.2f}")
        print(f"Периметр прямокутника: {perimeter:.2f}")

    elif choice == "2":
        try:
            r = float(input("Введіть радіус: "))
        except ValueError:
            print("Помилка: введіть число.")
            return

        if r <= 0:
            print("Радіус повинен бути більшим за нуль.")
            return

        area = math.pi * r ** 2
        circumference = 2 * math.pi * r

        print(f"Площа кола: {area:.2f}")
        print(f"Довжина кола: {circumference:.2f}")

    else:
        print("Неправильний вибір фігури.")


# Робота зі списками, кортежами та словниками
def data_structures():
    grades = [78, 90, 85, 96, 72]
    subjects = ("Математика", "Фізика", "Програмування")

    student = {
        "ім'я": "Настя",
        "курс": 2,
        "оцінки": grades
    }

    print("\nСписок оцінок:", grades)
    print("Кортеж предметів:", subjects)
    print("Словник студента:", student)

    print("Найвища оцінка:", max(grades))
    print(f"Середній бал: {sum(grades) / len(grades):.1f}")


# Приклад використання ітератора
def iterator_example():
    subjects = ("Математика", "Фізика", "Програмування")
    subject_iterator = iter(subjects)

    print("\nПредмети через ітератор:")

    while True:
        try:
            print(next(subject_iterator))
        except StopIteration:
            break


# Генератор квадратів парних чисел
def even_squares(n):
    for number in range(1, n + 1):
        if number % 2 == 0:
            yield number ** 2


def generator_example():
    try:
        n = int(input("Введіть число від 1 до 100: "))
    except ValueError:
        print("Помилка: введіть ціле число.")
        return

    if n < 1 or n > 100:
        print("Число має бути від 1 до 100.")
        return

    print("Квадрати парних чисел:")

    for value in even_squares(n):
        print(value, end=" ")

    print()


# Головне меню програми
def main():
    while True:
        print("\n===== ГОЛОВНЕ МЕНЮ =====")
        print("1 - Факторіал числа")
        print("2 - Геометричні фігури")
        print("3 - Списки, кортежі та словники")
        print("4 - Ітератор")
        print("5 - Генератор")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            factorial()
        elif choice == "2":
            geometry()
        elif choice == "3":
            data_structures()
        elif choice == "4":
            iterator_example()
        elif choice == "5":
            generator_example()
        elif choice == "0":
            print("Програму завершено.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
