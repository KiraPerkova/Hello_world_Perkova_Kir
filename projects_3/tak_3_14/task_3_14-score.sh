#!/bin/bash
echo "1) Студенты с оценкой выше 80:"
awk '$2 > 80 {print}' students.txt

echo -e "\n2) Студенты с оценкой ниже 70:"
awk '$2 < 70 {print}' students.txt

echo -e "\n3) Первая строка файла:"
awk 'NR==1 {print}' students.txt

