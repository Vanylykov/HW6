result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Обидва аргументи повинні бути числами.")
    if a < b:
        raise ValueError("Перший аргумент не може бути меншим за другий.")
    if b > 100:
        raise IndexError("Другий аргумент не може бути більшим за 100.")
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль недопустиме.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (TypeError, ValueError, IndexError, ZeroDivisionError, KeyError) as e:
        print(f"Помилка з ключем '{key}' та значенням '{data.get(key)}': {e}")

print("Результат:", result)