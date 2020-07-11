# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:03:41 2020

@author: cara_
"""
import settings
from dicts import dict_make
from deadlines import find_time, give_soonest_task


dict_make("walk dog", 2020, 9, 20, "pets")
print(settings.task_list)
print(find_time(settings.task_list[0]))

print(give_soonest_task(settings.task_list))
