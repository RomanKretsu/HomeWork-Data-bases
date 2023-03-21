# 1. Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INTEGER, genre TEXT
# 2. Создать функции:
#   1. Добавить фильм (заполнение делать с клавиатуры)
#   2. Получения данных обо всех фильмах
#   3. Получения данных об одном фильме по id
#   0. Выход
# 3. Функции вызывать в цикле, чтоб у пользователя был выбор.

import sqlite3

#  Создаем базу данных movies.db
conn = sqlite3.connect('movies.db')
#  Создаем объект cursor, который позволяет нам взаимодействойвать с базой данных и добавлять записи
cursor = conn.cursor()
#  Создаем таблицу с четырьмя полями (название, год, жанр): movie_id, name TEXT, release_year INTEGER, genre TEXT
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, release_year INTEGER, genre TEXT) ''')

# Создаем функцию movie(name, release_year, genre) ввода данных о фильмах (название, год, жанр)
def movie(name, release_year, genre):
    cursor.execute('''INSERT INTO movies (name, release_year, genre) VALUES (?, ?, ?)''',
                   (name, release_year, genre))
    # Сохраняем данные name, release_year, genre о внесенных фильмах в файл movies
    conn.commit()

# Создаем функцию получения данных обо всех фильмах
def data_allmovies():
    # Выбираем при помощи SELECT * FROM ... WHERE все данные о внесенных в базу фильмах
    cursor.execute('''SELECT * FROM movies''')
    # Заносим данные в переменную b
    b = cursor.fetchall()
    # При помощи цикла выводим данные по всем записям
    for i in b:
        print('******************************')
        print(i)
        print('№ фильма:           ', i[0])
        print('Название фильма:    ', i[1])
        print('Год выпуска фильма: ', i[2])
        print('Жанр фильма:        ', i[3])
        print('******************************')

# Создаем функцию получения данных об одном фильме по id
def data_onemovie(movie_id):
    # Выбираем при помощи SELECT * FROM ... WHERE данные по одному id (по одному фильму
    cursor.execute('''SELECT * FROM movies WHERE movie_id =?''', (movie_id,))
    # Заносим данные в переменную c
    c = cursor.fetchall()
    # При помощи цикла выводим данные по одной внесенной записи
    for i in c:
        print('******************************')
        print(i)
        print('№ фильма:           ', i[0])
        print('Название фильма:    ', i[1])
        print('Год выпуска фильма: ', i[2])
        print('Жанр фильма:        ', i[3])
        print('******************************')

# Создаем бесконечный цикл, в котором будут работать 3 функции:
# 1. Ввод данных о фильмах
# 2. Получение данных обо всех фильмах
# 3. Получение данных об одном фильме по id
while True:
    a = int(input('Введите данные: 1. Добавить фильм. 2. Получения данных обо всех фильмах. '
                  '3. Получения данных об одном фильме. 0. Выход:   '))

    if a == 1:
        print('Ввод данных о фильме: ')
        name = input('Введите название фильма: ')
        release_year = int(input('Введите год выхода фильма: '))
        genre = input('Введите жанр фильма: ')
        # работает функция "Ввод данных о фильмах"
        movie(name, release_year, genre)

    elif a == 2:
        print('Получение данных обо всех фильмах в базе данных: ')
        # работает функция "Получение данных обо всех фильмах"
        data_allmovies()


    elif a == 3:
        print('Получения данных об одном фильме по id: ')
        movie_id = int(input('Введите id фильма:  '))
        # работает функция "Получение данных об одном фильме по id"
        data_onemovie(movie_id)

    # Выход из программы
    elif a == 0:
        print('Выход')
        break

