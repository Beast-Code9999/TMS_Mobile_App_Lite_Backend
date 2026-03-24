from django.urls import path
from .views import CourseListView, CourseDetailView, ModuleListView, AssessmentListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('<int:course_id>/modules/', ModuleListView.as_view(), name='module-list'),
    path('<int:course_id>/modules/<int:module_id>/assessments/', AssessmentListView.as_view(), name='assessment-list'),
]