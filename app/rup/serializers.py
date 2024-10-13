from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"


class RupEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RupEntry
        fields = "__all__"


class RupFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RupFile
        fields = "__all__"


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reminder
        fields = "__all__"
