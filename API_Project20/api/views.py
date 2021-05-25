from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# No need to write separat function in just 3 lines CRUD ready ::)
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	# if we have more number of classes then define this permission globally in setting file
	authentication_classes = [BasicAuthentication]
	# permission_classes = [IsAuthenticated]
	# permission_classes = [AllowAny] #or we separate multiple pemission by using ,
	permission_classes = [IsAdminUser]  #only those user whose staff status is true