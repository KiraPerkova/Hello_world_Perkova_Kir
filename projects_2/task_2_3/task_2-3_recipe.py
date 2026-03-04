name = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"СРЕДА ЭНДО\n")
    file.write(f"Параметры:\n")
    file.write(f"\tКонцентрация агара: {agar}%\n")
    file.write(f"\tТемпература стерилизации:{temperature}\n")

print("Файл 'recipe.txt' успешно сформирован!")
