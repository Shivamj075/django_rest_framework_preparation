from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# Session authentication and for this we need to add extra login logout facility 
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	# if we have more number of classes then define this permission globally in setting file
	authentication_classes = [SessionAuthentication]
	# permission_classes = [IsAuthenticated]
	# permission_classes = [IsAuthenticatedOrReadOnly]
	permission_classes = [DjangoModelPermissions]  #by this we can give specific comm. that I want to give to particylar user
	permission_classes = [DjangoModelPermissionsOrAnonReadOnly] #now anoym. user will read

	