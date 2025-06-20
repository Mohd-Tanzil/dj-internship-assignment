import logging
import time
from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(username, email):
    logger.info(f"Simulating sending welcome email to {username} at {email}...")
    time.sleep(5)
    logger.info(f" Welcome email sent to {username}!")
    return f"Email sent to {email}"
