import requests
import numpy as np
import pandas as pd
from datetime import datetime


def main():
    print("===Демонстрация работы установленных пакетов===\n")

    # 1. Демонстрация работы с requests
    print("1. Работа с библиотекой requests:")
    try:
        response = requests.get("https://httpbin.org/json")
        if response.status_code == 200:
            data = response.json()
            print(f"   Успешный запрос к API")
            print(f"   Заголовок ответа: {data.get('slideshow', {}).get('title', 'N/A')}")
        else:
            print(f"   Ошибка запроса: {response.status_code}")
    except Exception as e:
        print(f"   Ошибка при выполнении запроса: {e}")

    print()

    # 2. Демонстрация работы с numpy
    print("2. Работа с библиотекой numpy:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"   Массив: {arr}")
    print(f"   Среднее значение: {np.mean(arr)}")
    print(f"   Сумма элементов: {np.sum(arr)}")

    # Создание матрицы
    matrix = np.random.randint(1, 10, (3, 3))
    print(f"   Случайная матрица 3x3:\n{matrix}")

    print()

    # 3. Демонстрация работы с pandas
    print("3. Работа с библиотекой pandas:")

    # Создание DataFrame
    data = {
        'Имя': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий'],
        'Возраст': [25, 30, 35, 28, 32],
        'Зарплата': [50000, 60000, 75000, 55000, 68000],
        'Город': ['Москва', 'СПб', 'Москва', 'Казань', 'СПб']
    }

    df = pd.DataFrame(data)
    print("   DataFrame сотрудников:")
    print(df.to_string(index=False))

    print(f"\n   Средний возраст: {df['Возраст'].mean():.1f}")
    print(f"   Средняя зарплата: {df['Зарплата'].mean():.0f}")

    # Группировка по городам
    city_stats = df.groupby('Город').agg({
        'Возраст': 'mean',
        'Зарплата': 'mean'
    }).round(1)

    print("\n   Статистика по городам:")
    print(city_stats)

    print(f"\n=== Проект успешно выполнен! ===")
    print(f"Время выполнения: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()