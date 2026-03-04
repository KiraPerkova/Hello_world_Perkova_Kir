seq = ["ATATACGCGTA", "CTTCGGNGGA"]

print("Работа с последовательностями ДНК:")
print("-" * 30)

for sequence in seq:
    print(f"\nПоследовательность: {sequence}")
    print("Построчно:")
    
    # Выводим последовательность по одному символу
    for nucleotide in sequence:
        print(nucleotide)
    
    print("---")

print("\nЦикл выполнен")