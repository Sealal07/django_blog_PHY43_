from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

# endpoint:  /register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)#сохранили данные отправленные post запросом со стороны клиента
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан')
    else: #обработка метода get
        form = RegisterForm()
    return render(request, 'users/register.html',
                  {'form':form})





# Create your views here.
