from django.shortcuts import render,   HttpResponse

# Create your views here.
def welcome_func(request):
    # print(dir(request))
    # return "Welcome to our application..!"
    # return HttpResponse ("welcome to our application")  #new vebsite vrti add honar
    # return HttpResponse("<h1> welcome amol in new page<h1>")

    # return HttpResponse("<h1> welcome amol in new page</h1><br>hi</h6")
    
    return render(request, "home.html")