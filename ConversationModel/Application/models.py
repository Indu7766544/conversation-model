from django.db import models
from nltk.tokenize import sent_tokenize


# Create your models here.
class Conversation(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    summary = models.TextField(blank=True, null=True)  # New field for summary

def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = self.generate_summary()
            

def generate_summary(self):
        # Basic summarization: taking the first 3 sentences
        sentences = sent_tokenize(self.body)
        return ' '.join(sentences[:3])
