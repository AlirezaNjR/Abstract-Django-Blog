from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm
from Accounts.models import CustomUserModel
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUserModel()
            user.username = cd['username']
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.email = cd['email']
            user.bio = cd['bio']
            user.telegram = cd['telegram']
            user.site = cd['site']
            user.instagram = cd['instagram']
            user.image = cd['image']
            if len(cd['password1']) >= 8:
                if (cd['password1'] == cd['password2']):
                    user.set_password(cd['password1'])
                    user.save()
                    return redirect('Accounts:SignIn')
                else:
                    pass
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

# ! ------------------ Profile ------------------
def profile(request,id):
    user = CustomUserModel.objects.get(id=id)
    return render(request,'registration/profile.html',{'User':user})