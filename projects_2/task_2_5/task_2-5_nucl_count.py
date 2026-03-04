def analyze_dna(sequence):
    # Приведение последовательности к верхнему регистру
    upper_sequence = sequence.upper()
    
    # Подсчет каждого нуклеотида
    count_a = upper_sequence.count('A')
    count_t = upper_sequence.count('T')
    count_g = upper_sequence.count('G')
    count_c = upper_sequence.count('C')
    
    # Общая длина последовательности
    total_length = len(upper_sequence)
    
    # Вывод результатов
    print("\n=== Анализ последовательности ДНК ===\n")
    print(f"Введите последовательность ДНК: {sequence}")
    print(f"\nПоследовательность в верхнем регистре: {upper_sequence}")
    print("\nПодсчёт нуклеотидов:")
    print(f"A: {count_a}")
    print(f"T: {count_t}")
    print(f"G: {count_g}")
    print(f"C: {count_c}")
    print(f"\nОбщая длина: {total_length} нуклеотидов")
    
    # Вычисление процентного содержания
    if total_length > 0:
        print("\nПроцентное содержание каждого нуклеотида:")
        print(f"A: {(count_a / total_length * 100):.1f}%")
        print(f"T: {(count_t / total_length * 100):.1f}%")
        print(f"G: {(count_g / total_length * 100):.1f}%")
        print(f"C: {(count_c / total_length * 100):.1f}%")
    else:
        print("\nПоследовательность пуста, невозможно вычислить процентное содержание.")

# Основная часть программы
if __name__ == "__main__":
    # Ввод пользовательской строки
    user_input = input("Введите последовательность ДНК: ")
    analyze_dna(user_input)