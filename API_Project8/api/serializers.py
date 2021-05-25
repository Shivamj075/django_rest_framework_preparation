from rest_framework import serializers
from .models import Student


#validator

class StudentSerializer(serializers.ModelSerializer):
	def start_with_r(value):
		if value[0].lower()!='r':
			raise serializers.ValidationError('Name should start with R')

	name = serializers.CharField(validators=[start_with_r])

	class Meta:
		model = Student
		fields = ['name','roll','city']
	

	#field level validation
	def validate_roll(self,value):
		if value>=200:
			raise serializers.ValidationError("Seat Full")
		return value

	#object level validation
	def validate(self,data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower()=='dhoni' and ct.lower()!='ranchi':
			raise serializers.ValidationError('City must be Ranchi!')
		return data