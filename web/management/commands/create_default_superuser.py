import time
from loguru import logger

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create default superuser by variables from env!"

    def handle(self, *args, **options):
        if (
            settings.DJANGO_SUPERUSER_PASSWORD
            and settings.DJANGO_SUPERUSER_USERNAME
            and settings.DJANGO_SUPERUSER_EMAIL
        ):
            users = User.objects.all()
            if not users:
                User.objects.create_superuser(
                    username=settings.DJANGO_SUPERUSER_PASSWORD,
                    email=settings.DJANGO_SUPERUSER_EMAIL,
                    password=settings.DJANGO_SUPERUSER_PASSWORD,
                    is_active=True,
                    is_staff=True,
                )
                logger.info(f"Superuser {settings.DJANGO_SUPERUSER_PASSWORD} was created!")
