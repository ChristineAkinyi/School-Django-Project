from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from api.serializers import ClassPeriodSerializer, CourseSerializer, MinimalClassPeriodSerializer, MinimalCourseSerializer, MinimalStudent_ClassSerializer, MinimalStudentSerializer, MinimalTeacherSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import ClassPeriod
from course.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from classroom.models import Classroom
from teacher.models import Teacher
from rest_framework import status

# Create your views here.
class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name: 
            Students = Students.filter(first_name = first_name)
        country = request.query_params.get("country")
        if country:
            Students = Students.filter(country = country)
        serializer = StudentSerializer(student, many=True)
        serializer = MinimalStudentSerializer(student, many = True)
        return Response(serializer.data)
       
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)
    
    def add_to_class(self, student, class_id):
        student_class = Classroom.objects.get(id=class_id)
        student_class.students.add(student)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)  
    
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        serializer = MinimalTeacherSerializer(teacher, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_class(self, teacher, class_id):
        classroom = Classroom.objects.get(id=class_id)
        classroom.teacher = teacher
        classroom.save()
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        serializer = MinimalCourseSerializer(course, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassroomListViews(APIView):
    def get(self, request):
        student_class = Classroom.objects.all()
        serializer = ClassroomSerializer(student_class, many=True)
        serializer = MinimalStudent_ClassSerializer(student_class, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassroomSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class ClassroomDetailView(APIView):
    def get(self, request,id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    
    def put(self, request,id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassPeriodListViews(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        serializer = MinimalClassPeriodSerializer(classperiod, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =ClassPeriodSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request,id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod= ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        classperiod = ClassPeriod(teacher=teacher, course=course)
        classperiod.save()
        return Response(status=status.HTTP_201_CREATED)
    
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
