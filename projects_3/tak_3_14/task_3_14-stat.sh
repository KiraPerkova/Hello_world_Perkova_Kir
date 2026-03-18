#!/bin/bash
#1 Сумма всех оценок:
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "1) Сумма оценок: $sum"
#2 Средняя оценка
avg=$(awk '{sum += $2; count++} END {print sum / count}' students.txt)
echo "2) Средняя оценка: $avg"
#3 Максимальная оценка
max=$(awk 'NR==1{max=$2} $2 > max{max=$2} END {print max}' students.txt)
echo "3) Максимальная оценка: $max"

