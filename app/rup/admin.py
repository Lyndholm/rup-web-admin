from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "group",
        "email",
        "phone_number",
    )
    list_filter = [
        "group",
    ]
    search_fields = [
        "name",
        "surname",
        "patronymic",
        "group",
        "email",
        "phone_number",
        "tg_id",
        "came_from",
    ]


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = [
        "name",
    ]


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone_number",
        "email",
    )
    search_fields = [
        "name",
        "address",
        "phone_number",
        "email",
        "comment",
    ]


@admin.register(models.RupEntry)
class RupEntryAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "semester",
        "academic_year",
        "statement_number",
    )
    search_fields = [
        "student__name",
        "subject__name",
        "semester",
        "academic_year",
        "statement_number",
    ]


@admin.register(models.RupFile)
class RupFileAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "file",
    )
    search_fields = [
        "student__name",
    ]


@admin.register(models.Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "student",
    )
    list_filter = [
        "date",
    ]
    search_fields = [
        "student__name",
    ]


@admin.register(models.BotPhrase)
class BotPhraseAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "value",
    )
    search_fields = [
        "key",
        "value",
    ]
