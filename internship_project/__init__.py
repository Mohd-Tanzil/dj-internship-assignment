import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()  # Load .env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')

app = Celery('internship_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Use REDIS_URL from .env
app.conf.broker_url = os.getenv('REDIS_URL')

app.autodiscover_tasks()
