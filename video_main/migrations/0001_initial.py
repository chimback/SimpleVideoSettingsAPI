# Generated by Django 3.2.2 on 2021-05-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoList',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=200)),
                ('author_name', models.CharField(db_column='AUTHOR_NAME', max_length=30)),
                ('image', models.ImageField(upload_to='img/')),
                ('view_number', models.IntegerField(db_column='VIEW_NUMBER')),
                ('uploaded_at', models.DateField(auto_now_add=True, db_column='UPLOADED_AT')),
            ],
            options={
                'db_table': 'video_list',
                'managed': False,
            },
        ),
    ]