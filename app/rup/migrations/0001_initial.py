# Generated by Django 5.1.1 on 2024-10-09 10:40

import django.core.validators
import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotPhrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=128, unique=True, verbose_name='Ключ')),
                ('value', models.CharField(max_length=2048, verbose_name='Фраза')),
            ],
            options={
                'verbose_name': 'Фраза бота',
                'verbose_name_plural': 'Фразы бота',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('address', models.CharField(blank=True, max_length=256, null=True, verbose_name='Адрес')),
                ('phone_number', models.CharField(blank=True, max_length=256, null=True, verbose_name='Номер(-а) телефона(-ов)')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=128, null=True, verbose_name='Отчество')),
                ('group', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}$')], verbose_name='Номер группы')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator('^(?:\\+7|8)\\s?\\(?\\d{3}\\)?\\s?\\d{3}-?\\d{2}-?\\d{2}$')], verbose_name='Номер телефона')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='ID пользователя Telegram')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата напоминания')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='rup.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Напоминание',
                'verbose_name_plural': 'Напоминания',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RupEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('semester', models.SmallIntegerField(verbose_name='Семестр')),
                ('academic_year', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{4}\\/\\d{4}$')], verbose_name='Учебный год дисциплины')),
                ('attestations', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Зачет'), (2, 'Зачет с оценкой'), (3, 'Экзамен'), (4, 'Курсовая работа')], max_length=7, verbose_name='Виды аттестаций')),
                ('credit_units', models.CharField(blank=True, max_length=10, null=True, verbose_name='Количество часов (з.е.)')),
                ('statement_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер ведомости на ликвидацию расхождений')),
                ('deadline', models.DateField(verbose_name='Срок сдачи')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rup_entries', to='rup.department', verbose_name='Предмет')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rup_entries', to='rup.student', verbose_name='Студент')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rup_entries', to='rup.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'РУП',
                'verbose_name_plural': 'РУПы',
                'ordering': ['-id'],
            },
        ),
    ]
