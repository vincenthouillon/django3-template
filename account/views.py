from django.shortcuts import redirect, render

from account.forms import UserAdminCreationForm


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'register.html', {'form': form})
