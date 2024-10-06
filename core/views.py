from django.shortcuts import render,redirect
from core.models import ContactUs, Newsletter

def home(request):
    return render(request, 'index.html')

def single(request):
    return render(request, 'single.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact_Us = ContactUs(fname=fname, lname=lname, email=email, subject=subject, message=message)
        Contact_Us.save()
        return redirect('home')
    else:
        return render(request, 'index.html')
    
def newsletter(request):
    if request.method == "POST":
        sub_email = request.POST.get('sub_email')

        news = Newsletter(sub_email=sub_email,)
        news.save()

        return redirect('home')
    else:
        return render(request, "index.html")

