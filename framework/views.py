from django.shortcuts import render, redirect
from .models import Framework
from .forms import FrameworkForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def acercade(request):
    return render(request, 'acercade.html')

def crear(request):
    print('creando..')
    if request.method == 'POST':  
        form = FrameworkForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    else:  
        form = FrameworkForm()  
    return render(request,'crear.html',{'form':form}) 

def editar(request, id):
    framework = Framework.objects.get(id=id)
    form = FrameworkForm(instance = framework)
    if request.method == 'POST':  
        form = FrameworkForm(request.POST, instance=framework)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass  
    context = {
        'framework': framework,
        'form': form
    }  
    return render(request,'editar.html', context) 

def eliminar(request, id):
    framework = Framework.objects.get(id=id)  
    framework.delete()  
    return redirect('/index')

def index(request):
    frameworks = Framework.objects.all()  
    return render(request,'index.html',{'frameworks':frameworks})  

def layout(request):
    return render(request, 'layout.html')

