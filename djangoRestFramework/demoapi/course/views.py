from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer


# Create your views here.

class GetAllCourseAPI(APIView):
	def get(self, request):
		list_course = Course.objects.all()
		mydata = GetAllCourseSerializer(list_course, many=True)
		return Response(data=mydata.data, status=status.HTTP_200_OK)
	
	def post(self, request):
		mydata = CourseSerializer(data=request.data)
		if not mydata.is_valid():
			return Response('sai du lieu', status=status.HTTP_400_BAD_REQUEST)
		title = mydata.data['title']
		content = mydata.data['content']
		price = mydata.data['price']
		cs = Course.objects.create(title=title, price=price, content=content)
		return Response(data=cs.id, status=status.HTTP_200_OK)