from django.db import models

# Create your models here.


class Notebook(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Note(models.Model):
    created_on = models.DateTimeField("created_on")
    note_title = models.CharField(max_length=50)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title
