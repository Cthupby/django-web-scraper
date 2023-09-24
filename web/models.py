from django.db import models


class ExtractedNews(models.Model):
    news_id = models.CharField(
        unique=True,
        max_length=200,
        verbose_name="Уникальный идентификатор новости",
    )
    url = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Прямая ссылка на новость",
    )
    title = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Заголовок новости",
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации новости",
    )
    text = models.TextField(
        null=True,
        blank=True,
        verbose_name="Полный текст новости",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
