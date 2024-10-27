from django.db import models

class InputFromsModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.IntegerField(help_text='Enter 6 digit roll number')
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
