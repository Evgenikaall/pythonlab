import math

g = 9.8


def fall_time_calculation():
    height = float(input("Введите высоту в метрах: "))
    while height < 0:
        print("Число должно быть больше 0. Попробуйте еще раз.")
        height = float(input("Введите высоту в метрах: "))

    time_of_fall = math.sqrt(2 * height / g)
    return time_of_fall


if __name__ == '__main__':
    print(f"Время падения объекта: {fall_time_calculation()} секунд.")
