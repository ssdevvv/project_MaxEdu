from django.db import models
from django.utils import timezone

class Advertisement(models.Model):
    # Другие поля модели
    updated_at = models.DateTimeField(auto_now=True)

    def last_updated(self):
        if self.updated_at.date() == timezone.now().date():
            return f"<span style='color: #FF0000'>Сегодня в {self.updated_at.time()}</span>"
        else:
            return self.updated_at

    last_updated.allow_tags = True
    last_updated.short_description = "Последнее обновление"