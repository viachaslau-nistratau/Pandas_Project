"""
Дан датафрем со следующими колонками:
name - имена работников
age - возраст
salary - заработная плата
Необходимо посчитать топ - 10 заработных плат, и отсортировать по убыванию.
Исходными данными является строка со словарем.
Чтобы преобразовать строку в словарь используется функция le(),
из библиотеки literal_eval. В шаблоне показано считывание и
преобразование данных в словарь. Вам необходимо преобразовать словарь
в DataFrame и произвести указанные вычисления.
Колонке с индексами дайте название 'TOP'.
Выведите полученный DataFrame.

Sample Input:
{'age': {0: 36, 1: 41, 2: 34, 3: 48, 4: 20, 5: 41, 6: 44, 7: 46, 8: 46, 9: 47,
10: 24, 11: 46, 12: 44, 13: 28, 14: 32},
'name': {0: 'Colli', 1: 'Dudly', 2: 'Ann', 3: 'Colli', 4: 'Colli', 5: 'Dudly',
6: 'Colli', 7: 'Ann', 8: 'Ann', 9: 'Bil', 10:'Colli', 11: 'Ann', 12: 'Colli',
13: 'Colli', 14: 'Colli'},
'salary': {0: 37518,1: 10028, 2: 63981, 3: 75254, 4: 43372, 5: 91670,
6: 75874, 7: 81422, 8: 44411, 9: 142465, 10: 13796, 11: 57226, 12: 57615,
13: 12763, 14: 28102}}

Sample Output:
TOP   name  age  salary
0      Bil   47  142465
1    Dudly   41   91670
2      Ann   46   81422
3    Colli   44   75874
4    Colli   48   75254
5      Ann   34   63981
6    Colli   44   57615
7      Ann   46   57226
8      Ann   46   44411
9    Colli   20   43372
"""
from ast import literal_eval as le
# обязательно подключаем библиотеку pandas
import pandas as pd

df = le(input())
# меняем местами стобцы
df = pd.DataFrame(df, columns = ['name', 'age', 'salary'])
# сортируем по столбцу 'salary', по убыванию, удаляем старые индексы
df = df.sort_values(by=['salary'], ascending = False).reset_index(drop=True)
# переименовываем столбец индексов в ТОР
df.rename_axis("TOP", axis='columns', inplace=True)
# выбираем первые 10 строк
df = df.head(10)
print(df)

"""
На вход подается строка со словарем, который необходимо преобразовать 
в DataFrame ( в предыдущем шаге показано как выделить из строки словарь, 
не забудьте подключить библиотеку).
Выведите только те строки датафрейма, возраст (колонка age) которых 
находится в интервале между числами [2;4] (включая границы).
Колонке с индексами дайте название 'YOUNG'.
Выведите полученный DataFrame.

Sample Input:
{'age': {0: 3, 1: 8, 2: 1, 3: 3, 4: 8, 5: 7, 6: 7, 7: 3, 8: 3, 9: 2, 10: 8, 11: 2, 
12: 2, 13: 5, 14: 7, 15: 4, 16: 4, 17: 3, 18: 9, 19: 8}, 
'animal': {0: 'dog', 1: 'cat', 2: 'dog', 3: 'dog', 4: 'dog', 5: 'cat', 
6: 'cat', 7: 'snake', 8: 'dog', 9: 'cat', 10: 'dog', 11: 'dog', 
12: 'dog', 13: 'dog', 14: 'dog', 15: 'dog', 16: 'dog', 17: 'snake', 
18: 'snake', 19: 'cat'}, 
'name': {0: 'Kaa', 1: 'Murzik', 2: 'Kaa', 3: 'Kaa', 4: 'Strelka', 
5: 'Strelka', 6: 'Strelka', 7: 'Kaa', 8: 'Kaa', 9: 'Kaa', 10: 'Kaa', 
11: 'Pushok', 12: 'Pushok', 13: 'Bobik', 14: 'Strelka', 15: 'Pushok', 
16: 'Kaa', 17: 'Pushok', 18: 'Strelka', 19: 'Kaa'}, 
'priority': {0: 'yes', 1: 'no', 2: 'yes', 3: 'yes', 4: 'yes', 5: 'no', 
6: 'yes', 7: 'yes', 8: 'yes', 9: 'no', 10: 'yes', 11: 'yes', 12: 'yes', 
13: 'yes', 14: 'yes', 15: 'yes', 16: 'yes', 17: 'yes', 18: 'yes', 19: 'no'}, 
'visits': {0: 3, 1: 4, 2: 1, 3: 3, 4: 3, 5: 4, 6: 3, 7: 1, 8: 1, 9: 2, 10: 3, 
11: 1, 12: 3, 13: 3, 14: 3, 15: 3, 16: 3, 17: 3, 18: 3, 19: 2}}

Sample Output:
YOUNG  age animal    name priority  visits
0        3    dog     Kaa      yes       3
3        3    dog     Kaa      yes       3
7        3  snake     Kaa      yes       1
8        3    dog     Kaa      yes       1
9        2    cat     Kaa       no       2
11       2    dog  Pushok      yes       1
12       2    dog  Pushok      yes       3
15       4    dog  Pushok      yes       3
16       4    dog     Kaa      yes       3
17       3  snake  Pushok      yes       3
"""
from ast import literal_eval as le
# обязательно подключаем библиотеку pandas
import pandas as pd

df = le(input())
df = pd.DataFrame(df)
# # переименовываем столбец индексов в YOUNG
df.rename_axis("YOUNG", axis='columns', inplace=True)
df1 = df[df['age'] <= 4]
df2 = df1[df1['age'] >= 2]
print(df2)

"""
Дан датафрем со следующими колонками:
name - имена работников
age - возраст
salary - заработная плата
specialization - специализация работы
Необходимо посчитать средний возраст и заработную плату работников 
в зависимости от специализации. Отсортировать полученный результат по 
возрастанию среднего возраста.
На вход подается строка со словарем, который необходимо преобразовать в 
DataFrame ( в предыдущем шаге показано как выделить из строки словарь, 
не забудьте подключить библиотеку).
Колонке с индексами дайте название 'RATING'.
Выведите полученный DataFrame.

Sample Input:
{'age': {0: 36, 1: 41, 2: 34, 3: 48, 4: 20, 5: 41, 6: 44, 7: 46, 8: 46, 9: 47, 
10: 24, 11: 46, 12: 44, 13: 28, 14: 32, 15: 24, 16: 36, 17: 36, 18: 48, 19: 43, 
20: 35, 21: 41, 22: 29, 23: 46, 24: 35}, 
'name': {0: 'Colli', 1: 'Dudly', 2: 'Ann', 3: 'Colli', 4: 'Colli', 
5: 'Dudly', 6: 'Colli', 7: 'Ann', 8: 'Ann', 9: 'Bil', 10: 'Colli', 
11: 'Ann', 12: 'Colli', 13: 'Colli', 14: 'Colli', 15: 'Colli', 16: 'Colli', 
17: 'Colli', 18: 'Colli', 19: 'Bil', 20: 'Bil', 21: 'Dudly', 
22: 'Dudly', 23: 'Ann', 24: 'Bil'}, 
'salary': {0: 37518, 1: 10028, 2: 63981, 3: 75254, 4: 43372, 5: 91670, 
6: 75874, 7: 81422, 8: 44411, 9: 142465, 10: 13796, 11: 57226, 
12: 57615, 13: 12763, 14: 28102, 15: 62579, 16: 126370, 17: 99752, 
18: 127615, 19: 30344, 20: 96977, 21: 74491, 22: 17023, 23: 98024, 
24: 39242}, 
'specialization': {0: 'DE', 1: 'Analitics', 2: 'DS', 3: 'DE', 4: 'DE', 
5: 'Analitics', 6: 'DE', 7: 'DS', 8: 'DS', 9: 'Planning', 10: 'DE', 11: 'DS', 
12: 'DE', 13: 'DE', 14: 'DE', 15: 'DE', 16: 'DE', 17: 'DE', 18: 'DE', 
19: 'Planning', 20: 'Planning', 21: 'Analitics', 22: 'Analitics', 
23: 'DS', 24: 'Planning'}}

Sample Output:
RATING           age        salary
specialization                    
DE              35.0  63384.166667
Analitics       38.0  48303.000000
Planning        40.0  77257.000000
DS              43.6  69012.800000
"""
import numpy as np
from ast import literal_eval as le
import pandas as pd

df = le(input())
df = pd.DataFrame(df)
# группируем по столбцу 'specialization' и подсчитываем средний возраст
# и среднюю зарплату
df = df.groupby('specialization')[['age', 'salary']].mean()
# сортировка по возрасту
df = df.sort_values(by=['age'], ascending = True)
# переименовываем столбец индексов в RATING
df.rename_axis("RATING", axis='columns', inplace=True)
print(df)

"""
В переменных df1 и df2 содержатся два словаря со следующими ключами:
df1: price - стоимость, type - тип продукта, availability- признак наличия продукта
df2: prod_id- id продукта, rating - оценка покупателей
Необходимо преобразовать два словаря в DataFrames. 
В df1 добавить колонку prod_id, где значениями будет являться 
последовательность от 1 до 25.
После этого объединить два Dataframe в один. 
Все пустые значения заменить на 0. И посчитать среднюю цену и с
редний рейтинг продуктов, которые есть в наличии (колонка availability = yes) 
по типам продуктов. Вывести DataFrame со средней стоимостью и рейтингом.
Колонке с индексами дайте название 'Prod_market'.
Выведите полученный DataFrame.

Sample Input:
df1 = {'availability': {0: 'yes', 1: 'no', 2: 'yes', 3: 'yes', 4: 'yes', 5: 'no',
                        6: 'yes', 7: 'yes', 8: 'yes', 9: 'no', 10: 'yes', 11: 'yes',
                        12: 'yes', 13: 'yes', 14: 'yes', 15: 'yes', 16: 'yes', 17: 'yes',
                        18: 'yes', 19: 'no', 20: 'no', 21: 'no', 22: 'no', 23: 'yes',
                        24: 'no'},
        'price': {0: 772, 1: 2114, 2: 876, 3: 78, 4: 1326, 5: 783, 6: 654, 7: 388,
                  8: 1840, 9: 2123, 10: 1667, 11: 969, 12: 1693, 13: 1486, 14: 1827,
                  15: 1724, 16: 1443, 17: 2220, 18: 1768, 19: 1732, 20: 1689, 21: 1011,
                  22: 156, 23: 1229, 24: 358},
       'type': {0: 'dairy', 1: 'meat', 2: 'dairy', 3: 'dairy', 4: 'porridge',
                5: 'porridge', 6: 'porridge', 7: 'dairy', 8: 'dairy', 9: 'dairy',
                10: 'dairy', 11: 'fish', 12: 'fish', 13: 'sweets', 14: 'porridge',
                15: 'fish', 16: 'dairy', 17: 'fish', 18: 'porridge', 19: 'dairy',
                20: 'porridge', 21: 'sweets', 22: 'sweets', 23: 'sweets', 24: 'dairy'}}
df2 = {'prod_id': {0: 19, 1: 24, 2: 17, 3: 3, 4: 24, 5: 7, 6: 11, 7: 15, 8: 7, 9: 19,
                   10: 19, 11: 18, 12: 24, 13: 12, 14: 18, 15: 11, 16: 18, 17: 21,
                   18: 13, 19: 12},
       'rating': {0: 3, 1: 8, 2: 1, 3: 3, 4: 8, 5: 7, 6: 7, 7: 3, 8: 3, 9: 2, 10: 8,
                  11: 2, 12: 2, 13: 5, 14: 7, 15: 4, 16: 4, 17: 3, 18: 9, 19: 8}}
                  
Sample Output:
Prod_market        price    rating
type                              
dairy        1091.375000  1.875000
fish         1716.428571  5.000000
porridge     1395.000000  3.714286
sweets       1293.250000  4.500000
"""
import pandas as pd
from ast import literal_eval as le

df1, df2 = map(le, input().split('-'))
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)

# создание объекта Series c названием колонки prod_id и значениями от 1 до 25
id_prod = pd.Series((x for x in range(1, 25)), name='prod_id')

# объединение Dataframe and Series - 2 способа
# df1 = pd.concat([df1, id_prod], axis=1) - 1 способ
df1 = pd.merge(df1, id_prod, left_index=True, right_index=True)  # 2 способ
# слияние двух Dataframe по df1, замена пустых значений на 0
df3 = pd.merge(df1, df2, how="left").fillna(0)
# посчитать среднюю цену и средний рейтинг продуктов, которые есть в
# наличии (колонка availability = yes) по типам продуктов.
# Выводим DataFrame со средней стоимостью и рейтингом.
df4 = df3[df3['availability'] == 'yes'].groupby('type')[['price','rating']].mean()
# переименовываем столбца индексов в Prod_market
df4.rename_axis("Prod_market", axis='columns', inplace=True)
print(df4)
