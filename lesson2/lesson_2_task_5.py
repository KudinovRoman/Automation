month = int(input("Напишите номер месяца: "))

def month_to_season (season):
    if season in [1, 2, 3]:
        print("Зима")
    elif season in [4, 5, 6]:
        print("Весна")
    elif season in [7, 8, 9]:
        print("Лето")
    elif season in [10, 11, 12]:
        print("Осень")
    else:
        print("Ты дурак?")

month_to_season(month)
    