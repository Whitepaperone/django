from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def actor_list(request):
    pass
@api_view(['GET'])
def actor_detail(request):
    pass
@api_view(['GET'])
def movie_list(request):
    pass
@api_view(['GET'])
def movie_detail(request):
    pass
@api_view(['GET'])
def review_list(request):
    pass
@api_view(['GET','PUT','DELETE'])
def review_detail(request):
    pass
@api_view(['GET'])
def create_review(request):
    pass