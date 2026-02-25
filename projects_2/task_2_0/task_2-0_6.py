file_path = r"C:\Users\пользователь\Desktop\Перькова_КЮ\output.txt"
info = "Имя: Кира\n Фамилия: Перькова\n Воозраст: 18\n Группа: 4731204/50001"
with open(file_path, 'w', encoding='utf-8')
as file:
    file.write(info)
print("Содержимое файла output.txt:")