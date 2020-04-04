from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import sqlite3
from .forms import ImageForm

def images(request):
    return render(request, 'images/images.html')


def upload_artwork(request): 
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'images/images.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('<a href="http://localhost:8000/">Upload Successful. Click here for homepage!</a>')