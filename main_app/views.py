from django.shortcuts import render

# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')

def animals_index(request):
  pass

def animals_details(request):
  pass