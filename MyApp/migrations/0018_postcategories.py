# Generated by Django 4.2.1 on 2023-07-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0017_contentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True, unique=True)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tblpostcategories',
                'ordering': ('category_name',),
            },
        ),
    ]
