from django.core.mail import send_mail
# from Config.settings import EMAIL_HOST_USER # ! For use Email
from django.shortcuts import redirect, render
from .models import EmailSubscriptionsModel
from .forms import EmailSubscriptionsForm, ContactForm
# Create your views here.

def subscription_view(request):
    if request.method == 'POST':
        print(request.path)
        form = EmailSubscriptionsForm(request.POST)
        if form.is_valid():
            Subscription = EmailSubscriptionsModel()
            Subscription.email = form.cleaned_data['email']
            Subscription.save()
            return redirect('Post:Home')


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject='Contact', 
                message=cd['message'], 
                from_email=cd['email'], 
                recipient_list=['EMAIL_HOST_USER','']
                )

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def about_page_view(request):
    return render(request,'about.html')

