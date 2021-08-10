# Generated by Django 3.2.6 on 2021-08-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('team_id', models.CharField(max_length=32)),
                ('item', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('restaurant', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
