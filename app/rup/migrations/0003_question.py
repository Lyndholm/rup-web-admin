# Generated by Django 5.1.1 on 2024-10-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rup', '0002_department_comment_student_came_from_rupfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-id'],
            },
        ),
    ]
