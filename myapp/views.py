from myapp.forms import MyForm, CommentForm
from django.shortcuts import render, redirect
from datetime import date
from myapp.models import Request, Comment

def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def testimonial_page(request):

    if request.method == 'POST':
        today = date.today()
        form = Comment(name=request.POST['name'],
                       message=request.POST['message'],
                       date=today.strftime('%d.%m.%Y'))
        form.save()
        return redirect('testimonial')
    else:
        form = CommentForm()

    comms = Comment.objects.all()

    return render(request, 'testimonial.html', context={'comms': comms})

def contact_page(request):

    if request.method == 'POST':
        today = date.today()
        form = Request(name=request.POST['name'], phone=request.POST['phone'], date=request.POST['date'], message=request.POST['message'])
        form.save()
        return redirect('contact')
    else:
        form = MyForm()

    return render(request, 'contact.html')