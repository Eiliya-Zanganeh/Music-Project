from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class UserModel(AbstractUser):
    age = models.IntegerField(verbose_name='سن', null=True, blank=True)
    country = models.CharField(max_length=300, verbose_name='کشور', null=True, blank=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['username']

    def __str__(self):
        return self.username


class MusicModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    music = models.FileField(upload_to='musics', verbose_name='موزیک')
    user = models.ForeignKey(UserModel, verbose_name='کاربر', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Music'
        verbose_name = 'موزیک'
        verbose_name_plural = 'موزیک ها'
        ordering = ['music']

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    music = models.ForeignKey(MusicModel, on_delete=models.CASCADE, related_name="comments", verbose_name='موزیک')
    text = models.TextField(verbose_name='متن')
    date = models.DateTimeField(auto_now=True, verbose_name='زمان')

    class Meta:
        db_table = 'Comment'
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return str(self.date)

