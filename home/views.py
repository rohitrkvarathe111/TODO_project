from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from home.models import Entry
from django.urls import reverse
from django.contrib import messages


def home(request):
    return render(request, 'home.html')




# Create your views here.
@login_required(login_url='login')
def mainpage(request):
    user = request.user
    data = Entry.objects.filter(user=user)
    return render(request, 'mainpage.html', {'data': data})

#    data = Entry.objects.all()
#    return render (request, 'mainpage.html',{'data':data})
#    return render(request, 'mainpage.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('Uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('Pass1')
        pass2 = request.POST.get('Pass2')
        if User.objects.filter(username=username).exists():
            msg = "Username already exists. Choose a different username."
            return render (request, 'signup.html',{'msg':msg})
#            return HttpResponse("Username already exists. Choose a different username.")
        if not (username and email and pass1 and pass2):
            msg = "Please fill in all fields."
            return render (request, 'signup.html',{'msg':msg})
#            return HttpResponse("Please fill in all fields.")
        if pass1!=pass2:
            msg = "your password are not same"
            return render (request, 'signup.html',{'msg':msg})
#            return HttpResponse("your password are not same")
        
        if User.objects.filter(email=email).exists():
            msg = "Email address already exists. Choose a different email."
            return render (request, 'signup.html',{'msg':msg})
#            return HttpResponse("Email address already exists. Choose a different email.")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')
        


    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)  
            return redirect('mainpage')
        else:
            msg = "Username and password are incorrect!!"
            return render (request, 'login.html',{'msg':msg})
 #           return HttpResponse("Username and password are incorrect!!")
        
    return render(request, 'login.html')


@login_required(login_url='login')
def Logoutpage(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print("Logged-in user:", user.username)
        data = Entry.objects.filter(user=user)
        
        if request.method =='POST':
            no = request.POST['no']
            date = request.POST['date']
            task = request.POST['task']
            if Entry.objects.filter(user=user, no=no).exists():
                msg = "Task with this Task number already exists."
            else:
                Entry.objects.create(user=user, no=no, date=date, task=task)
                msg = "Task saved"

            return render(request, 'mainpage.html', {'msg': msg, 'data': data})
        else:
            return HttpResponse("not found")


'''
            Entry.objects.create(user=user, no=no, date=date, task=task)

            msg = "Task saved"
            
            return render (request, 'mainpage.html',{'msg':msg,'data': data })
        else:
            return HttpResponse("not found")
 '''       

@login_required(login_url='login')
def delete_todo(request, no):
    print(no)
    Entry.objects.get(no=no).delete()
    return redirect('mainpage')

    
#def edit(request):
#    return render(request, 'edit.html')



from django.shortcuts import render, get_object_or_404

@login_required(login_url='login')
def edit(request, no):
    entry = get_object_or_404(Entry, no=no, user=request.user)

    if request.method == 'POST':
        
        entry.no = request.POST['no']
        entry.date = request.POST['date']
        entry.task = request.POST['task']
        entry.save()
        return redirect('mainpage')

    
    return render(request, 'edit.html', {'entry': entry})




















