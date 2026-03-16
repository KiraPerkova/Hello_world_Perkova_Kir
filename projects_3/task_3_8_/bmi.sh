#!/bin/bash
echo "Введите вашу массу (в кг):"
read mass

echo "Введите ваш рост (в метрах):"
read height

bmi=$(echo "scale=0; $mass / ($height * $height)" | bc)

echo "Ваш индекс массы тела (ИМТ): $bmi"
