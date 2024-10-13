from rest_framework import viewsets

from . import models, serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class RupEntryViewSet(viewsets.ModelViewSet):
    queryset = models.RupEntry.objects.all()
    serializer_class = serializers.RupEntrySerializer


class RupFileViewSet(viewsets.ModelViewSet):
    queryset = models.RupFile.objects.all()
    serializer_class = serializers.RupFileSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = models.Reminder.objects.all()
    serializer_class = serializers.ReminderSerializer
