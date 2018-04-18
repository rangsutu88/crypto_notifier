"""
Configures the schedules that will run in the application
"""
from celery.beat import crontab
from app.mod_crypto.tasks import post_crypto_emergency, post_telegram_notification


app_schedules = {
    post_crypto_emergency.__qualname__ : {
        "task": f"app.mod_crypto_tasks.{post_crypto_emergency.__qualname__}",
        'schedule': crontab(minute="10"),
    },
    post_telegram_notification.__qualname__: {
        "task": f"app.mod_crypto_tasks.{post_telegram_notification.__qualname__}",
        "schedule": crontab(minute="10")
    }
}