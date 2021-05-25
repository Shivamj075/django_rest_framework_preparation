from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# Session authentication and for this we need to add extra login logout facility 
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	# authentication_classes = [SessionAuthentication]
	# permission_classes = [DjangoModelPermissionsOrAnonReadOnly] #now anoym. user will read

	