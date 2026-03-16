#!/bin/bah

echo "Сщздание файлов..."

# Цико for для создания файлов
for i in {1..10}
do
    touch "test$i.txt"
    echo "Сщздан файл: test$i.txt"
done

echo "----------------------"
echo "Удаление файлов в обратном порядке"

# Цикл while для удаления файлов
counter=10
while [ $counter -ge 1 ]
do
    rm "test$counter.txt"
    echo "Удален файл: test$counter.txt"
    counter=$((counter - 1))
done

echo "Готово!"
