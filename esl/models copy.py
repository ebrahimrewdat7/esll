from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .validators import file_size

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "admin"), (2, "instructor"), (3, "learner"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    picture = models.ImageField(default=False, upload_to='user_pic')


class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    phoneNo = PhoneNumberField(unique=True, null=False, blank=False)
    document = models.FileField(upload_to='doc_pic')
    id_pic = models.ImageField(upload_to='id_pic')

    def __str__(self):
        return self.name


class Dictionary(models.Model):
    signId = models.AutoField(primary_key=True)
    signImage = models.ImageField(upload_to='pics')
    textForSign = models.TextField(max_length=25)



class VideoLecture(models.Model):
    id = models.AutoField(primary_key=True)
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video_lecture", validators=[file_size])

class BeginnerVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.OneToOneField(VideoLecture,  on_delete=models.CASCADE)
    type = models.CharField(max_length=20)


class IntermediateVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.OneToOneField(VideoLecture,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)


class AdvancedVideo(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.OneToOneField(VideoLecture,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
class Beginner(models.Model):
    id = models.AutoField(primary_key=True)
    dictionary = models.OneToOneField(Dictionary,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)


class Intermediate(models.Model):
    id = models.AutoField(primary_key=True)
    dictionary = models.OneToOneField(Dictionary,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)


class Advanced(models.Model):
    id = models.AutoField(primary_key=True)
    dictionary = models.OneToOneField( Dictionary,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)


# video call
# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FeedBackLearner(models.Model):
    id = models.AutoField(primary_key=True)
    Learner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class FeedBackInstructor(models.Model):
    id = models.AutoField(primary_key=True)
    Instructor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()