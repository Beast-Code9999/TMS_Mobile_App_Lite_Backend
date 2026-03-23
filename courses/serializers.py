from rest_framework import serializers
from .models import Course, Module, Assessment

# Serializers with nested read-only relationships for reponse

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'title', 'due_date', 'description']


class ModuleSerializer(serializers.ModelSerializer):
    assessments = AssessmentSerializer(many=True, read_only = True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'assessments']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'trainer', 'created_at', 'modules']
