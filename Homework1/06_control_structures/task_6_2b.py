# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
    octs = ip_address.split(".")
    correct = True

    if len(octs) == 4:
        for oct in octs:
            if not (oct.isdigit() and (int(oct) >= 0 and int(oct) < 256)):
                correct = False
    else:
        correct = False
    if correct:
        break
    print("Неправильный IP-адрес")
        


oct1 = int(octs[0])

if oct1 >= 1 and oct1 <=223:
   print("unicast")
elif oct1 >= 224 and oct1 <= 239:
   print("multicast")
elif ip_address == "255.255.255.255":
   print("local broadcast")
elif ip_address == "0.0.0.0":
   print("unassigned")
else:
   print("unused")