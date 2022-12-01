from json import load
from re import template
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

from app.models import JobPost

def hello(request):
    #template = loader.get_template('app\hello.html')
    context = {"name":"fesal"}
    #return HttpResponse(template.render(context, request))
    return render(request, 'app\hello.html', context)

job = {
    'title' : ['Wiraswasta', 'Petani','Pesulap'],
    'description' : ['Membuat Usaha Sendiri', 'Menanam Padi','Membuat Trick Mengagumkan']
}

def job_details(request, id):
    try:
        if id == 0:
            return redirect(reverse('home_root')) 
        
        job = JobPost.objects.get(id=id)

        data = {"job":job}

        return render(request, 'app/detail.html', data)

    except:
        return HttpResponseNotFound('Not Found!')

def job_list(requests):
    # list_of_job = "<ul>"
    # for i in range(0,len(job['title'])):
    #     list_of_job += f"<li>{job['title'][i]} : {job['description'][i]} <a href='{reverse('job_details', args=(i,))}'>Selengkapnya</a></li>"
    # list_of_job += "</ul>"

    jobs = JobPost.objects.all()

    data = {"jobs":jobs}

    return render(requests, 'app/index.html', data)