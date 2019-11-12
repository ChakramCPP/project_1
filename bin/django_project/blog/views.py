from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
posts=[
    {
        'author':'Chakrapani',
        'title':'Krsna Consciousness',
        'content':'Chant every day',
        'date_posted':'Nov 12'
    },
    {
        'author':'Chakrapani',
        'title':'Krsna Consciousness1',
        'content':'Chant every day1',
        'date_posted':'Nov 22'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
