from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()