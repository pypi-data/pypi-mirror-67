from django.db import models

DEFAULT_THEME = "default"

DEFAULT_THEME_CHOICES = [
    (DEFAULT_THEME, "Default"),
]


class ErrorSkin(models.Model):
    active = models.BooleanField(unique=True)
    theme = models.CharField(
        choices=DEFAULT_THEME_CHOICES, default=DEFAULT_THEME, max_length=100
    )
    logo = models.ImageField(null=True)
    background_image = models.ImageField(null=True)
    font = models.CharField(default="Montserrat", max_length=100)
