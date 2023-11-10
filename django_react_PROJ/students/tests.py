from django.test import TestCase
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializers import *

@api_view(['GET','POST'])
def students_list(request)
