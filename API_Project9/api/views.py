from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

#by default it contain GET like @api_view(['GET'])
# @api_view()
# def hello_world(request):
# 	return Response({'msg':'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
# 	if request.method == 'POST':
# 		print(request.data)
# 		return Response({'msg':'This is Post request'})



@api_view(['GET','POST'])
def hello_world(request):
	if request.method == 'GET':
		return Response({'msg':'This is GET Request'})
	if request.method == 'POST':
		print(request.data)
		return Response({'msg':'This is Post request'})

