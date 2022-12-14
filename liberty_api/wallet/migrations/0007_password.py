# Generated by Django 3.2.15 on 2022-09-08 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_auto_20220908_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wallet.user')),
                ('password', models.CharField(max_length=30)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('pin', models.IntegerField(max_length=4)),
            ],
        ),
    ]
