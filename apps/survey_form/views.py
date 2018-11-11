from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, "survey_form/index.html")

def result(request):
    return render(request, "survey_form/result.html")

def process(request):
    if request.method == "POST":
        if 'attempts' in request.session:
            request.session['attempts'] += 1
        else:
            request.session['attempts'] = 0

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        
        return redirect("/result")
    else:
        return redirect(request, "/")
