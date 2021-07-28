from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    original_word = models.CharField(max_length=255)
    translate_original_word = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255, default='', blank=True)
    create_date = models.DateTimeField('create_date', auto_now=True)
    # slug = models.SlugField()

    class Meta:
        ordering = ('-create_date',)

    def __str__(self) -> str:
        return self.original_word

    def get_absolute_url(self):
        return f'/{self.slug}'
