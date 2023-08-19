from django.db import models

# Create your models here.

class TarotCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tarot_cards/')
    keywords = models.TextField()
    upright_meaning = models.TextField()
    reversed_meaning = models.TextField()

    def __str__(self):
        return self.name