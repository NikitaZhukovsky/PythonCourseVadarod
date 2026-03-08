"""
Дан словарь, содержащий названия городов и их среднемесячные температуры за год в виде списка из 12 чисел.
Нужно определить город с самой высокой среднегодовой температурой и вывести все города,
где максимальная температура за год превышает 25 градусов.
"""

city_temperatures = {
    "Минск": [-8, -5, 0, 8, 15, 20, 22, 21, 15, 8, 0, -5],
    "Брест": [6, 7, 10, 15, 20, 25, 28, 28, 24, 18, 12, 8],
    "Витебск": [-12, -10, -2, 6, 13, 18, 20, 18, 12, 4, -5, -10],
    "Гомель": [2, 4, 8, 15, 22, 27, 30, 29, 24, 16, 9, 4]
}

avg_temperatures = {}

for city, temps in city_temperatures.items():
    avg_temp = sum(temps) / len(temps)
    avg_temperatures[city] = avg_temp

hottest_city = max(avg_temperatures, key=avg_temperatures.get)

print(f"Город с самой высокой среднегодовой температурой: {hottest_city}")

hot_cities = []

for city, temps in city_temperatures.items():
    if max(temps) > 25:
        hot_cities.append(city)

print(f"Города с температурой выше 25 градусов: {', '.join(hot_cities)}")

