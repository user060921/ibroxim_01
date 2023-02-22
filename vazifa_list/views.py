from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import vazifa



def register_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            context['error'] = 'Bunday username mavjud'
            return render(request, 'register.html', context)

        if password == password2:
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()
            return redirect('create_task')
        else:
            context['error'] = 'Parol bir xil emas'
    return render(request, 'register.html')


def login_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('create_taskl')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_task')
        else:
            context['error'] = 'Bunday foydalanuvchi mavjud emas!'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page(request):
    q = request.GET.get('q')
    tasks = vazifa.objects.filter(user=request.user)
    if q is not None:
        tasks = tasks.filter(Q(title__icontains=q) | Q(description__icontains=q))
    context = {
        'user_tasks_count': tasks.count(),
        'tasks': tasks,

    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create_task(request): 
    if request.method == 'POST':
        narxi = request.POST.get('narxi')
        title = request.POST.get('title')
        description = request.POST.get('description')
        sifati = request.POST.get('sifati')
        qushilgansana = request.POST.get('qushilgansana')

        # print(title, description, narxi,sifati,)
        task = vazifa.objects.create(
            user= request.user,
            title=title,
            narxi=narxi,
            description=description,
            sifati=sifati,
            qushilgansana=qushilgansana,
        )
        task.save()

        return redirect('create_task')

    return render(request, 'create_page.html')

@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(vazifa, pk=pk)
    task.delete()
    return redirect('home_page')

@login_required(login_url='login')
def detail_page(request,):
   
    tasks = vazifa.objects.filter(user=request.user)
    context = {
        'user_tasks_count': tasks.count(),
        'tasks': tasks,
    }
    return render(request, 'detail_page.html', context)





