from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filterset_fields = ['tg_id']

    @action(detail=False, methods=['get'], url_path='search/(?P<tg_id>[0-9]+)')
    def retrieve_by_tg_id(self, request, tg_id=None):
        try:
            student = self.queryset.get(tg_id=tg_id)
            serializer = self.get_serializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.Student.DoesNotExist:
            return Response(
                {"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND
            )


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


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class MeetingViewSet(viewsets.Meetings):
    queryset = models.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer
