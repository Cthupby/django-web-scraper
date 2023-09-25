from config.celery import app
from loguru import logger

from scrapy.start_scraper import main


@app.task
def check_news_task():
    logger.info("Check news started!")
    main()


app.conf.beat_schedule = {
    # Executes every 15 minutes
    "add-every-15-minutes": {
        "task": "web.tasks.check_news_task",
        "schedule": crontab(minute=15),
    },
}
