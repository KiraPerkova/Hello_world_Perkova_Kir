#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Ошибка: не хватает аргументов. Нужно передать имя гена и уровень экспрессии."
    exit 1
fi 

gene_name=$1
expression_level=$2

echo "Экспрессия гена $gene_name составляет $expression_level единиц"
