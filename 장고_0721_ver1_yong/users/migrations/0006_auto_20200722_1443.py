# Generated by Django 3.0.3 on 2020-07-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_board_b_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_title', models.CharField(max_length=30)),
                ('n_memo', models.TextField()),
                ('n_writer', models.CharField(max_length=20)),
                ('n_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
