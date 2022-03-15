# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint


ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
octs = ip_address.split(".")
correct = True

if len(octs) != 4:
   correct = False
else:
   for oct in octs:
      if not (oct.isdigit() and (int(oct) >= 0 and int(oct) < 256)):
         correct = False

if correct == False:
   print("Неправильный IP-адрес")
else:
   if int(octs[0]) >= 1 and int(octs[0]) <=223:
      print("unicast")
   elif int(octs[0]) >= 224 and int(octs[0]) <= 239:
      print("multicast")   
   elif ip_address == "255.255.255.255":
      print("local broadcast")
   elif ip_address == "0.0.0.0":
      print("unassigned")
   else:
      print("unused")
   