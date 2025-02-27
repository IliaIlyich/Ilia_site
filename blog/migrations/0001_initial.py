# Generated by Django 5.0.4 on 2024-07-18 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('excerpt', models.CharField(max_length=300)),
                ('image_name', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('slug', models.SlugField(default='')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('e_mail', models.EmailField(max_length=254, null=True)),
                ('posts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]
