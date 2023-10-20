from django.contrib import admin

from app.models import Product, Category, Blog, Contact, Comment, Wishlist, AboutBanner, User, SocialLinksType, \
    SocialLinks, Team

# Register your models here.

# admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Wishlist)
admin.site.register(AboutBanner)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(SocialLinksType)
admin.site.register(SocialLinks)
