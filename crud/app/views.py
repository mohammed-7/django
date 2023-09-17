from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.


def index(request):
    return render(request, "app/index.html")

# here we are inserting if loop coz we have to address the data either in post or get, now as we see in terminal that our python code is responsible to get the data from the front end.
# using return redirect function is to redirect the page back to home after insertion of the data and storing it into database. whenever there's post request we need to redirect it to home page
# now to store the data we need to import studentmodel by defining object std


def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        course = request.POST["course"]
        std = Student(name=name, course=course)
        std.save()
        return redirect("/")

    return render(request, "app/create.html")

# here at getdetails we are fetching data from db


def getdetails(request):
    data = Student.objects.filter(is_deleted=0)

    return render(request, "app/getdetails.html", {'data': data})


def update(request, id):

    std1 = Student.objects.get(id=id)

    print("Filter Result", std1)
    print("\n\n")
    std = Student.objects.get(id=id)
    print("Get Result", std)

    if request.method == "POST":
        std.name = request.POST["name"]
        std.course = request.POST["course"]
        std.save()
        return redirect("/getdetails")
    return render(request, "app/update.html", {"data": std})
