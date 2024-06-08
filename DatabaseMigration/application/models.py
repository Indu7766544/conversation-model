from django.db import models

# Create your models here.


import nltk
from nltk.tokenize import sent_tokenize
from django.db.models.signals import pre_save
from django.dispatch import receiver

nltk.download('punkt')

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Book)
def generate_summary(sender, instance, **kwargs):
    if not instance.summary:
        sentences = sent_tokenize(instance.content)
        instance.summary = ' '.join(sentences[:5])  # Simple summary using the first 5 sentences
