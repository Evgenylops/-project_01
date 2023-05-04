# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
###################################################################
print('Три песни звучат', my_favorite_songs[3][1] + my_favorite_songs[4][1] + my_favorite_songs[5][1], 'минут')
#  ответ: Три песни звучат 12.46 минут


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
#####################################################################

print('Три песни звучат', my_favorite_songs_dict['Easy'] + my_favorite_songs_dict['A Sorta Fairytale'] + my_favorite_songs_dict['Nowhere to Run'], 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
########################################################################################################
import random
my_favorite_songs = random.sample(my_favorite_songs, 3)
print(my_favorite_songs)


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

