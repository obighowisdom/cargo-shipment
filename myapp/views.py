from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
from .models import cons
from .models import comment
from .models import location
from .models import location_two



# Create your views here.

def index(request):


    com = comment.objects.all()
    
    return render(request, 'index.html', {'com':com})

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def track(request):


    # form = request.POST.get("identity")
    # fas = request.POST.get("true_value")
    # if request.method == 'POST':

    #     form = request.POST.get("identity")
    #     fas = request.POST.get("true_value")
    # elif fas == form:
    #      return redirect("index:about")

    # else:
    #     return redirect("index:contact")
       
    # else:
    #     return redirect("index:contact")
    # nice = ''
    # cool = ''
    
    if request.method == 'POST':
        nice = request.POST.get('identity')
        t_one = request.POST.get('identity_one')
        cool = request.POST.get('true_value')
        

        data = cons(caption=nice, true=t_one, trac_one=cool)
        data.save()

    
        if nice == cool:
            return redirect("index:result")
        
        elif t_one == cool:
            return redirect("index:loc_two")
        
            
        
        else:
            messages.success(request, f'Location not available, try again')
            return redirect("index:track")



    wis = cons.objects.all()

      

    

    return render(request, 'track.html', {'wis':wis})


def result(request):
    loc = location.objects.all()

    

    return render(request, 'result.html', {'loc':loc})

# location two

def details_two(request):
    loc_two = location_two.objects.all()

    return render(request, 'id_one.html', {'loc_two':loc_two})