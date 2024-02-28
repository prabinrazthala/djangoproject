from django.shortcuts import render

from myapp.models import ClassRoom

# Create your views here.

def root_page(request):
    return render(request,template_name="myapp/root_page.html")


def temp_inherit_home(request):
    return render(request,template_name="myapp/temp_inherit_home.html")

def portfolio(request):
    return render(request,template_name="myapp/portfolio.html")

def classroom(request):
    classrooms = [
        {"name": "One", "address": "KTM"},
        {"name": "Two", "address": "PKR"},
        {"name": "Three", "address": "BKT"},
        {"name": "Four", "address": "LTP"},
        {"name": "Four", "address": "LTP"},
    ]
    return render(request, template_name="myapp/classroom.html",
                  context={"classroom_name": "One", "location": "KTM", "classrooms": classrooms})
    
    
    
def student(request):
    
    students = [
    {"name": "Jon", "age": 21, "address": "KTM", "email": "jon@email.com"},
    {"name": "Jane", "age": 22, "address": "PKR", "email": "jane@email.com"},
    {"name": "Hary", "age": 23, "address": "BKT", "email": "hary@email.com"},
    {"name": "Ken", "age": 34, "address": "LTP", "email": "ken@email.com"},
]
    return render(request,template_name="myapp/student.html",context={"students":students})

def classroom_query_set(request):
    
    classrooms = ClassRoom.objects.all()
    
    return render(request,template_name="myapp/classroom_query_set.html", context={"classrooms":classrooms})
    
