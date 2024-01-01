from django.shortcuts import render, redirect
from app.forms import SignUpForm
from django.contrib.auth.decorators import login_required

from app.models import Room

def index(request):
    return render(request, 'app/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index-page')
        
    else:
        form = SignUpForm()
    
    return render(request, 'app/signup.html', {
        'form': form,
    })

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'app/rooms.html', {"rooms": rooms})