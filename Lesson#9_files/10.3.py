"""
Дан словарь:
days = { 1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thu', 6:'Fri', 7:’Sat’}
Записать его в файл построчно.
"""

days = {
    1: 'Sun',
    2: 'Mon',
    3: 'Tue',
    4: 'Wed',
    5: 'Thu',
    6: 'Fri',
    7: 'Sat'
}

with open('days.txt', 'w') as file:
    for k, v in days.items():
        file.write(str(k) + ":" + v + "\n")

