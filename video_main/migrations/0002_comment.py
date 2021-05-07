# Generated by Django 3.2.2 on 2021-05-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=30)),
                ('contents', models.TextField(db_column='CONTENTS', max_length=1000)),
                ('number_of_likes', models.IntegerField(db_column='NUMBER_OF_LIKES')),
                ('number_of_hates', models.IntegerField(db_column='NUMBER_OF_HATES')),
                ('author_like', models.BooleanField(db_column='AUTHOR_LIKE')),
                ('created_at', models.DateField(auto_now_add=True, db_column='CREATED_AT')),
                ('updated_at', models.DateField(auto_now=True, db_column='UPDATED_AT')),
            ],
            options={
                'db_table': 'comment_list',
                'managed': False,
            },
        ),
    ]