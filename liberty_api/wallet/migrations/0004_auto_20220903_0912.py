# Generated by Django 3.2.15 on 2022-09-03 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20220902_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='UPreference',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wallet.user')),
                ('image', models.ImageField(upload_to='upload_image')),
                ('ep_key', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='zzzz@yyy', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_answer1',
            field=models.TextField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_answer2',
            field=models.TextField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_question1',
            field=models.TextField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_question2',
            field=models.TextField(max_length=80, null=True),
        ),
    ]