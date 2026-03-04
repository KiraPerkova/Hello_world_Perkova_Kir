# Запрос ввода данных у пользователя
total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_capacity = int(input("Введите количество капсул в одной упаковке: "))

# Расчет с использованием операторов // и %
full_packs = total_capsules // pack_capacity  # целочисленное деление (полные упаковки)
remaining_capsules = total_capsules % pack_capacity  # остаток от деления

# Вывод результатов
print("\n--- Отчет фасованного цеха ---")
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {remaining_capsules}")
