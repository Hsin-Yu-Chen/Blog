# Generated by Django 3.0.3 on 2021-10-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='標題')),
                ('content', models.CharField(max_length=200, verbose_name='內容')),
            ],
        ),
    ]
