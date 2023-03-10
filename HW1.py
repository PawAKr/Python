# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict

item1 = 'Володя'
item2 = 22
item3 = 2.34
item4 = bytes('байты', encoding = 'utf-8')
item5 = ['Ivan', 23, 'Oleg', 'Jan']
item6 = (23, 15, 'Vlad')
item7 = ['v', 'g', 'a', 's']
item8 = {'Ivan', 23, 'Oleg', 'Jan'}
item9 = frozenset({1,2,3,4,5,6,7})
item10 = {'name': 'Vlad', 'age': 23}

print (item1)
print (item2)
print (item3)
print (item4)
print (item5)
print (item6)
print (item7)
print (item8)
print (item9)
print (item10)

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print (type(item1))
print (type(item2))
print (type(item3))
print (type(item4))
print (type(item5))
print (type(item6))
print (type(item7))
print (type(item8))
print (type(item9))
print (type(item10))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.

item11 = 'Vlad'
item12 = 'Nika'
item13 = 'Nika' " " + " " 'Vlad'
print(item13)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)

item14 = 'Nika' " " "," + " " 'Vlad'
print(item14)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

item15 = 'Nika' " " "+" + " " 'Vlad'
print(item15)


