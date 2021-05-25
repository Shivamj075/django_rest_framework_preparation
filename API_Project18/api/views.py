from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


# No need to write separat function in just 3 lines CRUD ready ::)
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer