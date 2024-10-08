from celery import shared_task
import random
import time

@shared_task
def my_task(arg1, arg2):
    print('inside the celery task.... Adding..')
    # Task logic here
    result = arg1 + arg2
    return result


@shared_task
def add(x, y):
    # Celery recognizes this as the `movies.tasks.add` task
    # the name is purposefully omitted here.
    time.sleep(10)
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)

