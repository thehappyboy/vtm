from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Q
from django.urls import reverse
from PIL import Image
from django.conf import settings


class CustomUserManager(UserManager):
    def search(self, query=None):
        queryset = self.get_queryset()
        if query is not None:
            or_lookup = (
                    Q(username__icontains=query)
                    | Q(first_name__icontains=query)
                    | Q(last_name__icontains=query)
                    | Q(email__icontains=query)
            )
            queryset = queryset.filter(or_lookup).distinct()

        return queryset


class User(AbstractUser):
    is_engineer = models.BooleanField(default=False)
    is_serviceman = models.BooleanField(default=False)
    is_workman = models.BooleanField(default=False)
    is_teamleader = models.BooleanField(default=False)
    department = models.CharField(max_length=50, blank=True, null=True, verbose_name='部门')
    section = models.CharField(max_length=50, blank=True, null=True, verbose_name='科室')
    age = models.PositiveSmallIntegerField(verbose_name='年龄')
    phone = models.CharField(max_length=30, null=True, blank=True)
    # picture = models.ImageField(upload_to='profile_pictures/%y/%m/%d/', default='default.png', null=True, blank=True)

    gender_choices = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices, default='M', verbose_name='性别')

    objects = CustomUserManager()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ("-date_joined",)

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return f'{self.username} ({self.get_full_name})'

    @property
    def get_user_role(self):
        if self.is_engineer:
            role = 'Engineer'
        elif self.is_serviceman:
            role = 'Serviceman'
        elif self.is_workman:
            role = 'Workman'

        return role

    def get_absolute_url(self):
        return reverse('profile_single', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     try:
    #         img = Image.open(self.picture.path)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             img.save(self.picture.path)
    #     except:
    #         pass
    #
    # def delete(self, *args, **kwargs):
    #     if self.picture.url != settings.MEDIA_URL + 'default.png':
    #         self.picture.delete()
    #     super().delete(*args, **kwargs)
