from django.shortcuts import render,HttpResponse,redirect
import random
		# random number between 1-100

# Create your views here.
def index(request):
    result=0
    if 'number' in request.session:
        if request.method=="POST":
            if "play" in request.POST:
                user_number=int(request.POST['user_number'])
                if user_number == request.session['number']:
                    result=1
                elif user_number>request.session['number']:
                    result=2
                else:
                    result=3
            else:
                del request.session['number']
                return redirect("/")
    else:
        rand=random.randint(1, 100) 
        request.session['number']=rand
    return render(request,"index.html",{'result':result,"user_result":request.session['number']})
