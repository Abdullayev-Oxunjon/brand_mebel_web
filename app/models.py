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


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    image2 = models.ImageField(upload_to="product2/")
    image3 = models.ImageField(upload_to="product3/", null=True, blank=True)
    image4 = models.ImageField(upload_to="product4/", null=True, blank=True)
    image5 = models.ImageField(upload_to="product5/", null=True, blank=True)

    title = models.CharField(max_length=155)
    rank = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    extra_description = models.TextField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(to="app.Category",
                                 on_delete=models.CASCADE,
                                 related_name='products')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount:

            discount_amount = self.price * (self.discount / 100)
            return self.price - discount_amount
        else:
            return self.price

    def __str__(self):
        return self.title


class Blog(BaseModel):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=155)
    text = models.TextField()
    mini_image = models.ImageField(upload_to='blog2/')
    mini_image2 = models.ImageField(upload_to='blog3/')
    user = models.ForeignKey(to="app.User",
                             on_delete=models.CASCADE,
                             related_name='blogs')
    extra_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.name


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


class Wishlist(models.Model):
    user = models.ForeignKey(to="app.User",
                             on_delete=models.CASCADE,
                             related_name="wishlists")
    product = models.ManyToManyField(to="app.Product",
                                     related_name='wishlists')

    def __str__(self):
        return self.user


class Cart(models.Model):
    user = models.ForeignKey(to="app.User",
                             on_delete=models.CASCADE,
                             related_name="carts")
    product = models.ManyToManyField(to="app.Product",
                                     through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(to="app.Cart",
                             on_delete=models.CASCADE)
    product = models.ForeignKey(to="app.Product",
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        if self.product.discount is not None:
            return self.quantity * self.product.discounted_price
        else:
            return self.quantity * self.product.price


class SocialLinksType(models.Model):
    title = models.CharField(max_length=155)
    icon = models.FileField(upload_to='images/icons/')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name


class SocialLinks(models.Model):
    user = models.ForeignKey(to="app.Team",
                             on_delete=models.CASCADE,
                             related_name="sociallinks")
    type = models.ForeignKey(to="app.SocialLinksType",
                             on_delete=models.CASCADE,
                             related_name="social_links")
    link = models.CharField(max_length=198)


class AboutBanner(models.Model):
    main_image = models.ImageField(upload_to='about/')
    since = models.CharField(max_length=155)
    title = models.CharField(max_length=155)
    description = models.TextField()

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
        regex=r'^\+?\d{1,15}$',
        message="Yaroqsiz telefon raqam !")
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
