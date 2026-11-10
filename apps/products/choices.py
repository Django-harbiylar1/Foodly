from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Kutilmoqda'
    CONFIRMED = 'confirmed', 'Tasdiqlangan'
    DELIVERING = 'delivering', 'Yetkazilmoqda'
    COMPLETED = 'completed', 'Yetkazildi'
    CANCELLED = 'cancelled', 'Bekor qilindi'