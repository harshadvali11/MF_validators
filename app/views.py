from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse
def insert_student(request):
    ESMFO=StudentMF()
    d={'ESMFO':ESMFO}

    if request.method=='POST':
        SMFDO=StudentMF(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Data is Created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_student.html',d)