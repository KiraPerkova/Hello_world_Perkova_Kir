#!/bin/bash

# Вывод заголовка таблицы
printf "%-15s %-6s %-6s %-6d %-6s\n" "Файл" "A" "T" "G" "C"

# Перебор всех .fasta файлов в папке
for file in *.fasta; do

# пропускаем пустые файлы
    if [ ! -s "$file" ]; then continue
    fi
# Извлечение последовательности,исключаем строки заголовков, объединяем последовательность в одну строку для подсчета
    sequence=$(grep -v "^" "$file" | tr -d '\n')
# Подсчет каждого нуклеотида
    a_count=$(echo "$sequence" | grep -o "A" | wc =1)
    t_count=$(echo "$sequence" | grep -o "T" | wc -1)
    g_count=$(echo "$sequence" | grep -o "G" | wc -1)
    c_count=$(echo "$sequence" | grep -o "C" | wc -1)
# Вывод строки с результатами
    printf "%-15s %-7d %-7d %-7d %-7d\n" "$file" "$a_count" "$t_count" "$g_count" "$c_count" 
done


