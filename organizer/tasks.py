from celery import shared_task


@shared_task()
def add_number2():
    return True

