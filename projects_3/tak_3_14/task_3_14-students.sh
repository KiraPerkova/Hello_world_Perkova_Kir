#!/bin/bash
echo "1) Только имена студентов:"
awk '{print $1}' students.txt

echo -e "\n2) Только оценки студентов:"
awk '{print $2}' students.txt

echo -e "\n3) Номер строки и имя:"
awk '{print NR, $1}' student.txt
