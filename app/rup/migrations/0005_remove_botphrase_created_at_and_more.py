# Generated by Django 5.1.1 on 2024-12-03 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0004_question_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botphrase',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='botphrase',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='reminder',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Отправлено'),
        ),
        migrations.AddField(
            model_name='rupentry',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Закрыт'),
        ),
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='botphrase',
            name='value',
            field=models.TextField(verbose_name='Фраза'),
        ),
        migrations.AlterField(
            model_name='department',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительно'),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата встречи')),
                ('comment', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='rup.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Встреча',
                'verbose_name_plural': 'Встречи',
                'ordering': ['-id'],
            },
        ),
    ]
