# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
net = input ("Введите IP-сеть в формате: 10.1.1.0/24: ")

ip, mask = net.split("/")
ip = ip.split(".")
mask = int(mask)
print(ip)
bin_mask = "1" * mask + "0" * (32-mask)
print(bin_mask)
ip_template = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""
oct1, oct2, oct3, oct4 = [int(bin_mask[0:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2)]

mask_template = """
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
print(mask_template.format(mask, oct1, oct2, oct3, oct4))