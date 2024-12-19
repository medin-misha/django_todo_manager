from django.db import models

# Create your models here.
class TodoItems(models.Model):
    title = models.CharField(max_length=250)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self) -> str:
        return f"{self.title}"