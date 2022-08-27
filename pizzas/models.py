from django.db import models

# Создайте здесь свои модели.
class Pizza(models.Model):
    """Пицца на выбор пользователем."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.name

class Topping(models.Model):
    """Топинги для пиццы"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name