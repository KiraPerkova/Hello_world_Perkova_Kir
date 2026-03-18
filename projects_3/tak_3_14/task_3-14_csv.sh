#!/bin/bash
echo "1) Названия товаров:"
awk -F ', ' '{print $2}' data.csv

echo -e "\n2) Товары дороже 20:"
awk -F ',' '$3 > 20 {rpint}' data.csv

echo -e "\n3) Общая стоимость:"
total=$(awk -F ',' '{sum += $3} END {print sum}' data.csv)
echo "Сумма: $total"
