from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from . forms import ContactForm

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(name, message, email, ['musa@gmail.com',], fail_silently=False,)
            return HttpResponse('lol')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    
    return render(request, 'contact/index.html', context)
