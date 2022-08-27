from django.contrib import admin

# Зарегистрируйте здесь ваши модели.

from .models import Pizza, Topping
admin.site.register(Pizza)
admin.site.register(Topping)