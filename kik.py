import psutil
import datetime
import json
import time
import os
import pyttsx3
from random import choice


# Путь к файлу с информацией о лимитах и запущенных программах
KILLIST_PATH = 'Killist.txt'

# Путь к файлу с информацией о запущенных программах
JSON_PATH = 'programs.json'

# Считываем информацию о лимитах из файла Killist.txt
with open(KILLIST_PATH, 'r') as f:
    # killist = [line.strip().split() for line in f.readlines()]
    killist = [[i[0], int(i[1]) * 60, i[2]] for i in [line.strip().split() for line in f.readlines()]]

# Создаем или загружаем информацию о запущенных программах из файла programs.json
if os.path.exists(JSON_PATH):
    with open(JSON_PATH, 'r') as f:
        programs = json.load(f)
else:
    programs = {}

# Время задержки в секундах
time_sleep = 3

while True:
    # Получаем текущую дату и время
    now = datetime.datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M:%S')

    # Проверяем каждую программу из списка на запущенность
    for name, limit, days in killist:
        # Проверяем, работает ли программа в текущий день недели
        if str(now.weekday() + 1) in days:
            # Проверяем, запущена ли программа
            if name in [p.name() for p in psutil.process_iter()]:
                # Получаем информацию о программе из словаря programs
                program_info = programs.get(current_date, {}).get(name, [days, 0, limit, [], True])

                # Вычисляем оставшееся время работы программы
                # remaining_time = program_info[2] - program_info[1]

                # Выводим информацию о программе в консоль
                # print(f'{name} работает. Осталось времени: {remaining_time} секунд.')

                # Если лимит времени превышен, закрываем программу
                if (program_info[1] >= limit and program_info[4]) or program_info[4] == False:
                    for p in psutil.process_iter():
                        if p.name() == name:
                            p.kill()
                            program_info[4] = False
                            # print(f'{name} закрыта.')

                            # Обновляем информацию о программе в словаре programs
                            program_info[3] += [current_time]
                            programs.setdefault(current_date, {})[name] = program_info
                            with open(JSON_PATH, 'w') as f:
                                json.dump(programs, f, indent=2)

                # Иначе обновляем информацию о программе в словаре programs
                else:
                    program_info[1] += time_sleep
                    programs.setdefault(current_date, {})[name] = program_info
                    with open(JSON_PATH, 'w') as f:
                        json.dump(programs, f, indent=2)

    # Ждем повторяем цикл
    time.sleep(time_sleep)
