from core.models import TimeStampedModel
from django.core import validators
from django.db import models
from multiselectfield import MultiSelectField


class Student(TimeStampedModel):
    name = models.CharField(
        "Имя",
        max_length=128,
        null=False,
        blank=False,
    )
    surname = models.CharField(
        "Фамилия",
        max_length=128,
        null=False,
        blank=False,
    )
    patronymic = models.CharField(
        "Отчество",
        max_length=128,
        null=True,
        blank=True,
    )
    group = models.CharField(
        "Номер группы",
        max_length=10,
        null=False,
        blank=False,
        validators=[
            validators.RegexValidator(
                r"^\d{3}-\d{3}$",
            ),
        ],
    )
    email = models.EmailField(
        "E-mail",
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        "Номер телефона",
        max_length=32,
        null=True,
        blank=True,
        validators=[
            validators.RegexValidator(
                r"^(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-?\d{2}-?\d{2}$"
            )
        ],
    )
    tg_id = models.BigIntegerField(
        "ID пользователя Telegram",
        unique=True,
        null=False,
        blank=False,
    )
    came_from = models.CharField(
        "Откуда перевелся",
        max_length=256,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["-id"]

    @property
    def full_name(self):
        parts = [self.surname, self.name, self.patronymic]
        return " ".join(part for part in parts if part)

    def __str__(self) -> str:
        return f"{self.full_name} ({self.group})"


class Subject(TimeStampedModel):
    name = models.CharField(
        "Название",
        max_length=128,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.name


class Department(TimeStampedModel):
    name = models.CharField(
        "Название",
        max_length=128,
        null=False,
        blank=False,
    )
    address = models.CharField(
        "Адрес",
        max_length=256,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        "Номер(-а) телефона(-ов)",
        max_length=256,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        "E-mail",
        null=True,
        blank=True,
    )
    comment = models.CharField(
        "Дополнительно",
        max_length=512,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.name


class RupEntry(TimeStampedModel):
    class AttestationTypes(models.IntegerChoices):
        TEST = 1, "Зачет"
        TEST_WITH_MARK = 2, "Зачет с оценкой"
        EXAM = 3, "Экзамен"
        COURSE_WORK = 4, "Курсовая работа"

    student = models.ForeignKey(
        Student,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="rup_entries",
        verbose_name="Студент",
    )
    subject = models.ForeignKey(
        Subject,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="rup_entries",
        verbose_name="Предмет",
    )
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rup_entries",
        verbose_name="Предмет",
    )
    semester = models.SmallIntegerField(
        "Семестр",
        null=False,
        blank=False,
    )
    academic_year = models.CharField(
        "Учебный год дисциплины",
        max_length=10,
        null=False,
        blank=False,
        validators=[
            validators.RegexValidator(
                r"^\d{4}\/\d{4}$",
            ),
        ],
    )
    attestations = MultiSelectField(
        choices=AttestationTypes.choices,
        blank=True,
        verbose_name="Виды аттестаций",
    )
    credit_units = models.CharField(
        "Количество часов (з.е.)",
        max_length=10,
        null=True,
        blank=True,
    )
    statement_number = models.CharField(
        "Номер ведомости на ликвидацию расхождений",
        max_length=32,
        null=True,
        blank=True,
    )
    deadline = models.DateField(
        "Срок сдачи",
    )

    class Meta:
        verbose_name = "РУП"
        verbose_name_plural = "РУПы"
        ordering = ["-id"]


class RupFile(TimeStampedModel):
    student = models.ForeignKey(
        Student,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="rup_files",
        verbose_name="Студент",
    )
    file = models.FileField(
        "Файл",
    )

    class Meta:
        verbose_name = "Файл РУП"
        verbose_name_plural = "Файлы РУПов"
        ordering = ["-id"]


class Reminder(models.Model):
    date = models.DateField(
        "Дата напоминания",
    )
    student = models.ForeignKey(
        Student,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="reminders",
        verbose_name="Студент",
    )

    class Meta:
        verbose_name = "Напоминание"
        verbose_name_plural = "Напоминания"
        ordering = ["-id"]


class BotPhrase(TimeStampedModel):
    key = models.CharField(
        "Ключ",
        max_length=128,
        unique=True,
        null=False,
        blank=False,
    )
    value = models.CharField(
        "Фраза",
        max_length=2048,
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.key

    class Meta:
        verbose_name = "Фраза бота"
        verbose_name_plural = "Фразы бота"
        ordering = ["-id"]


class Question(models.Model):
    question = models.TextField(
        "Вопрос",
        null=False,
        blank=False,
    )
    answer = models.TextField(
        "Ответ",
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["-id"]
