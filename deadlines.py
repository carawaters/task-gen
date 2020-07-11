from datetime import date


def find_time(task):
    """Gives the number of days from today until the deadline for a task.

    Args:
        task (list): The list for the task [task name (str), deadline (date), category (str)].

    Returns:
        time_left.days (int): The number of days from now until the task deadline.
    """
    task_date = task[1]
    time_left = task_date - date.today()
    return time_left.days


def sort_deadlines(task_list):
    """Takes the task list and sort by soonest deadline.

    Args:
        task_list (dict): The dictionary of tasks.

    Returns:
        deadline_sorted_tasks (list): A list of the tasks (which are lists themselves), sorted by ascending days
        until deadline.
    """
    days_left_tasks = []
    tasks = [*task_list.values()]
    for i in tasks:
        days_left_tasks.append([i[0], find_time(i), i[2]])
    deadline_sorted_tasks = sorted(days_left_tasks, key = lambda l:l[1])
    return deadline_sorted_tasks


def give_soonest_task(task_list):
    task = sort_deadlines(task_list)[0]
    return task
