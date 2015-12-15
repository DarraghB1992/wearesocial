from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from contact.forms import ContactView
from django.shortcuts import redirect
from django.core.mail import EmailMessage


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            email = EmailMessage(subject=request.POST.get('topic'), body=request.POST.get('message'),
                                 from_email="darragh1992@gmail.com", to=[request.POST.get('email')])
            email.send()
            my_form = form.save(commit=False)
            my_form.save()
            messages.add_message(request, messages.INFO, 'Your message has been set. Thank You')

            return redirect("/")

    else:
        form = ContactView()
    return render(request, 'contact.html', {'form': form})

