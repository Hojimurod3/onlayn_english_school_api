from rest_framework import serializers
from .models import Students,Teachers, Kurses, Lessons, Branch,Level

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["name", 'location']

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurses
        fields = ["title", 'max_students']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ["start_time", 'end_time']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['name', 'description']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'name', 'surname', 'phone', 'ielts']

class StudentsSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    level = LevelSerializer()
    time = TimeSerializer()
    kurs = KursSerializer()
    branch = BranchSerializer()

    class Meta:
        model = Students
        fields = ['title', 'phone', 'level', 'kurs', 'time', 'teacher', "branch"]