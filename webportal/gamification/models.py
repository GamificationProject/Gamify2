from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Game(models.Model):
    game_name = models.CharField(max_length = 100)
    game_description = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.game_name
    
class UserProfile(models.Model):
    BEGINNER = 0
    AMATEUR = 1
    PROFESSIONAL = 2
    EXPERT = 3
    LEVEL_CHOICE = ((BEGINNER, 'Beginner'), (AMATEUR, 'Amateur'), (PROFESSIONAL, 'Professional'), (EXPERT, 'Expert'))
    user = models.ForeignKey(User, unique = True, on_delete = models.CASCADE)
    dp = models.FileField(name = 'Profile_Picture')
    detail = models.CharField(max_length = 250, null = True)
    dob = models.DateField(null=True)
    level = models.IntegerField(choices = LEVEL_CHOICE, default = BEGINNER)

    def __str__(self):
        return str(self.user)

    def age(self):
        return (date.today() - self.dob) // timedelta(days = 365.2425)

    def dpurl(self):
        return str(self.dp.url)