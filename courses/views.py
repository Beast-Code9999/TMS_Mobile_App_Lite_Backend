from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Course, Module, Assessment
from .serializers import CourseSerializer, ModuleSerializer, AssessmentSerializer

# Handles listing all courses (GET) and creating a new course (POST)
# Requires authentication
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# Handles retrieving a single course (GET), updating (PUT/PATCH), and deleting (DELETE)
# Looks up course by its primary key (id)
# Requires authentication
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# Handles listing all modules for a specific course (GET) and creating a module (POST)
# Filters modules based on course_id from the URL (nested route)
# Requires authentication
class ModuleListView(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Module.objects.filter(course_id=self.kwargs['course_id'])

# Handles listing all assessments for a specific module (GET) and creating an assessment (POST)
# Filters assessments based on module_id from the URL (nested route)
# Requires authentication
class AssessmentListView(generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Assessment.objects.filter(module_id=self.kwargs['module_id'])