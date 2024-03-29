#Generic APIview and Model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# pk not required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)




# class StudentCreate(GenericAPIView, CreateModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer

# 	def post(self,request,*args,**kwargs):
# 		return self.create(request,*args,**kwargs)


# pk required
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)



# class StudentUpdate(GenericAPIView,UpdateModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer

# 	def put(self,request,*args,**kwargs):
# 		return self.update(request,*args,**kwargs)

# class StudentDestroy(GenericAPIView,DestroyModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer

# 	def delete(self,request,*args,**kwargs):
# 		return self.destroy(request,*args,**kwargs)









