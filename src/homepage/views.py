from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from images.models import Images
from images.forms import ImageForm
import sqlite3

template_name = 'homepage/home.html'
def home(request):
    return render(request, 'homepage/home.html')


def post_detail(request):
    c = Images.objects.values('image').order_by('-id')[:10]
    d = c[0]
    e = str(d) 
    g = e.split('/')[-1][:-2]
    h = g.split('/')[-1]
    pic1 = h

    j = c[1]
    k = str(j) 
    l = k.split('/')[-1][:-2]
    m = l.split('/')[-1]
    pic2 = m

    n = c[2]
    o = str(n) 
    p = o.split('/')[-1][:-2]
    q = p.split('/')[-1]
    pic3 = q

    ca = Images.objects.values('name', 'title').order_by('-id')[:10]
    da = ca[0]
    ea = str(da) 
    ga = ea.replace("{","").replace("}","").replace("'","").replace(",","")
    ha = ga.upper()
    ainfo1 = ha

    ia= ca[1]
    ja = str(ia) 
    ka = ja.replace("{","").replace("}","").replace("'","").replace(",","")
    la = ka.upper()
    ainfo2 = la

    ma = ca[2]
    na = str(ma) 
    oa = na.replace("{","").replace("}","").replace("'","").replace(",","")
    pa = oa.upper()
    ainfo3 = pa

    

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    return render(request, 'homepage/home.html', {'form': form, 'pic1':pic1, 'pic2':pic2, 'pic3':pic3, 'ainfo1':ainfo1, 'ainfo2':ainfo2, 'ainfo3':ainfo3,  })


    



   







