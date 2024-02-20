
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .forms import NewUserForm  # username, email, pass1, pass2
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def user_signup(request):
    if request.method == "POST":
        data = request.POST
        form = NewUserForm(data)
        if form.is_valid():
            user = form.save()  # user entry in auth_user table
            print(user)   #AparnaH
            messages.success(request, f"User '{user.username}' registered successfully. You can login here." )
            return redirect("user_signup")
        else:
            messages.error(request, "Unsuccessful signup. Invalid information.")
            return HttpResponse("unsuccessful signup")
    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request, template_name="register.html", context={"signup_form":form})
    

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # username, password
        if form.is_valid():
            user_name = form.cleaned_data.get("username")  # KapilD
            password = form.cleaned_data.get("password")    # Python@123
            # print(user_name, password)
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)  # verify -- auth_user -- return user object
        if user:
            login(request, user)   # session maintain -- django session table
            messages.success(request, "Logged in succesfully.")
            # return redirect("home_page")
            return HttpResponse("Success 1")
        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponse("success 2")

    elif request.method == "GET":
        return render(request, "login.html", {"login_form": AuthenticationForm()})
    

# username = "amolshinde"
# password = "amol1234"
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context

# def user_signup(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             ######################### mail system ####################################
#             htmly = get_template('user/Email.html')
#             d = { 'username': username }
#             subject, from_email, to = 'welcome', password
#             html_content = htmly.render(d)
#             ##################################################################
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login')
#     else:
#         form = NewUserForm()
#     return render(request, 'register.html', {'form': form, 'title':'register here'})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user:
#             form = login(request, user)
#             messages.success(request, f' welcome {username} !!')
#             return redirect('home_page')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form':form, 'title':'log in'})


def user_logout(request):
    logout(request)
    return redirect("user_login")