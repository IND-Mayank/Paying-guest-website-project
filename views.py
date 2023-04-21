from django.shortcuts import render
from django.http import HttpResponse
def test(request):
    return HttpResponse('testing the first page')
def pg(request):
    return render(request,'registration.html')
def page(request):
    return render(request,'room.html')
def res(request):
    return render(request,'reservation.html')
def PGres(request):
    return render(request,'PGres.html')
def yourpg(request):
    return render(request,'yourpg.html')    