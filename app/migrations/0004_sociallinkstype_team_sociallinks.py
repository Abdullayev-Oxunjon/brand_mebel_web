# Generated by Django 4.2.1 on 2023-10-19 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinksType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('icon', models.FileField(upload_to='images/icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('image', models.ImageField(upload_to='team/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=198)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='app.sociallinkstype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sociallinks', to='app.team')),
            ],
        ),
    ]
