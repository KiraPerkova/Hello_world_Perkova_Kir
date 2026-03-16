#!/bin/bash

for i in {1..20}
do
    # Если число четное, пропускаем итерацию
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi 

    # Если число 15, останавливаем цикл
    if [ $i -eq 15 ]; then
        break
    fi

    # Выводим нечетные числа
    echo $i
done
