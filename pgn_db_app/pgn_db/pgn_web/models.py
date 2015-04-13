from django.db import models
from helpers import findUndergradData
import requests

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=31, default=" ")
    last_name = models.CharField(max_length=31, default=" ")
    username = models.CharField(max_length=31, null=True)
    password = models.CharField(max_length=31, null=True)
    graduation_year = models.DateField(blank=True, null=True)
    major = models.CharField(max_length=31, default="Undeclared")
    linked_in = models.CharField(max_length=255, default="")
    image = models.CharField(max_length=255, blank=True, null=True)
    authenticated = models.BooleanField(default=False)
    access_token = models.CharField(max_length=31, default="")

    def sync(data):

        response = requests.get("https://api.linkedin.com/v1/people/~:(first-name,last-name,summary,picture-urls::(original),public-profile-url,educations)", headers={"Authorization": "Bearer " + data['access_token'], "Connection":"Keep-Alive"}, params={"format": "json"}).json()
        values = {
            "first_name": response['firstName'],
            "last_name": response['lastName'],
            "username": data['username'],
            "password": data['pass'],
            "image":  response['pictureUrls']['values'][0],
            "linked_in": response['publicProfileUrl'],
            "summary": response['summary'],
            "graduation_year": findUndergradData(response['educations']['values'], "endDate"),
            "major": findUndergradData(response['educations']['values'], "fieldOfStudy"),
            "authenticated": True,
            "access_token": data['access_token']
        }

        if Brother.objects.filter(first_name=values['first_name'], last_name=values['last_name']).exists():
            return ("success", values)
        else:
            return ("error", None)

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=31)

class Major(models.Model):
    name = models.CharField(max_length=63)

class Company(models.Model):
    contact = models.ManyToManyField(User)

class Job(models.Model):
    company = models.ForeignKey(Company)
    member = models.ForeignKey(User)
    title = models.CharField(max_length=63)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=255, null=True, blank=True)

class Brother(models.Model):
    first_name = models.CharField(max_length=31, default=" ", null=True)
    last_name = models.CharField(max_length=31, default=" ", null=True)
