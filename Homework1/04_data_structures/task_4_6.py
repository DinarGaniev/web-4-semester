# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

from re import template


ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route_list = ospf_route.split()
print(ospf_route_list)
result = {'Prefix': ospf_route_list[0],
          'AD_Metric': ospf_route_list[1].strip("[]"),
          'Next_Hop': ospf_route_list[3].strip(','),
          'Last_update': ospf_route_list[4].strip(','),
          'Outbound_Interface': ospf_route_list[5]}
template = '''
Prefix               {Prefix:15}
AD/Metri             {AD_Metric} 
Next-Hop             {Next_Hop} 
Last update          {Last_update}
Outbound Interface   {Outbound_Interface} 
'''
print(template.format(**result))
