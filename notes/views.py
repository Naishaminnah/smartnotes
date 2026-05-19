from django.shortcuts import render,redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
@login_required
def note_list(request):
    query=request.GET.get('q')
    notes=Note.objects.filter(user=request.user)

    if query:
        notes=notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request,'notes/note_list.html',({'notes':notes,'query':query}))

@login_required
def create_notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(user=request.user, title=title , content=content)

        return redirect('note_list')
    return render(request, 'notes/create_note.html')

@login_required
def delete_note(request , id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)   
        note.delete()
        return redirect('note_list')

@login_required
def edit_note(request , id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')
    return render(request , 'notes/edit_note.html' , {'note':note})


def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username,password=password)

        if user:
            login(request,user)
            return redirect('note_list')
       
    return render(request,'notes/login.html')


def signup_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        User.objects.create_user(username=username,password=password)

        return redirect('login')
    return render(request, 'notes/signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')