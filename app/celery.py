import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app',
             backend='rpc://',
             broker='amqp://',
             include=['accounts.tasks'])


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
