from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Home(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to="home/")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(BaseModel):
    image = models.ImageField(upload_to='product/')
    image2 = models.ImageField(upload_to='product2/')
    image3 = models.ImageField(upload_to='produc3/')
    image4 = models.ImageField(upload_to='produc4/')
    image5 = models.ImageField(upload_to='produc5/')
    title = models.CharField(max_length=155)
    rank = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(to="app.Category",
                                 on_delete=models.CASCADE,
                                 related_name='products')

    @property
    def discounted_price(self):
        discount_amount = self.price * (self.discount / 100)
        return self.price - discount_amount

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(max_length=25,
                                    validators=[phone_validator],
                                    null=True,
                                    blank=True,
                                    unique=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Comment(BaseModel):
    text = models.TextField()
    user = models.ForeignKey(
        to='app.User',
        on_delete=models.CASCADE,
        related_name='user_comments')
    blog_id = models.ForeignKey(
        to='app.Blog',
        on_delete=models.CASCADE,
        related_name='comments_blog')

    def __str__(self):
        return self.text


class Blog(BaseModel):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=155)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    message = models.TextField()
    user = models.ForeignKey(to="app.User",
                             on_delete=models.CASCADE,
                             related_name='contacts')

    def __str__(self):
        return self.user
