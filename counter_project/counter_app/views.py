from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    
    if 'counter' in request.session:
        print('key exists!')
        if request.method=='POST':
            if "tow" in request.POST:
                request.session['counter']=request.session['counter']+1
                return redirect("/")
            elif "user_inc_bt" in request.POST:
                number=int(request.POST["user_inc"])
                request.session['counter']=request.session['counter']+number
                return redirect("/")
        else:
            request.session['counter']=request.session['counter']+1
            print(request.session['counter'])
        request.session.save()
    else:
        print("key does NOT exist")
        request.session['counter']=1
    if 'counter2' in request.session:
        request.session['counter2']=request.session['counter2']+1
        print(request.session['counter2'])
        request.session.save()
    else: 
        request.session['counter2']=1
    return render(request,"counter.html")

def destroy_session(request):
    del request.session['counter']
    del request.session['counter2']
    return redirect("/")
