# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:27:26 2020

@author: cara_
"""

import settings
from datetime import date


# Put into dictionary of task no, task name, due date and category

def dict_make(name, year, month, day, category):
    """Creates a new or appends to the existing dictionary of tasks.

    Args:
        name (str): Task name.
        year (int): Year in full format (e.g. 2020).
        month (int): Month in full format (e.g. 09).
        day (int): Day in full format (e.g. 05).
        category (str): The type of task.
    """
    deadline = date(year, month, day)
    if len(settings.task_list) == 0:
        settings.task_list = {0: [name, deadline, category]}
    else:
        keys = settings.task_list.keys()
        new_key = max(keys) + 1
        settings.task_list[new_key] = [name, deadline, category]
    return None
