from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    state = models.enums = {
        'open'
        'close'
    }

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text =  models.CharField(max_length=500)

class Answer(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text =  models.CharField(max_length=500)
