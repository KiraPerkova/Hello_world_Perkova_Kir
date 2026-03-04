# Запрашиваем группы крови донора и пациента
donor_blood = input("Введите группу крови донора (0, A, B, AB): ").upper().strip()
recipient_blood = input("Введите группу крови пациента (0, A, B, AB): ").upper().strip()

# Проверяем корректность ввода
valid_groups = ["0", "A", "B", "AB"]

if donor_blood not in valid_groups or recipient_blood not in valid_groups:
    print("Ошибка: введите корректную группу крови (0, A, B, AB)")
else:
    # Проверяем возможность переливания
    # Переливание возможно, если:
    # 1. Группы совпадают, ИЛИ
    # 2. Донор имеет нулевую группу (универсальный донор)
    
    if donor_blood == recipient_blood or donor_blood == "0":
        print(f"Переливание возможно: донор {donor_blood} → пациент {recipient_blood}")
    else:
        print(f"Переливание НЕВОЗМОЖНО: донор {donor_blood} → пациент {recipient_blood}")