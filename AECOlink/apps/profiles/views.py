from django.shortcuts import render, redirect

from apps.profiles.forms import ClientForm


# Create your views here.
def index(request):
    return render(request, 'profile.html', {})

def profile(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('profiles: profile')

    else:
        form = ClientForm()

        return render(request, profile.html, {'form': form})
