from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"students", views.StudentViewSet)
router.register(r"subjects", views.SubjectViewSet)
router.register(r"departments", views.DepartmentViewSet)
router.register(r"rup-entries", views.RupEntryViewSet)
router.register(r"rup-files", views.RupFileViewSet)
router.register(r"reminders", views.ReminderViewSet)
