from django.shortcuts import render, redirect
from .forms import ControllerForm
from .models import Controller


def dashboard(request):
    controller = Controller.objects.first()

    if request.method == 'POST':
        form = ControllerForm(request.POST, instance=controller)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ControllerForm(instance=controller)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/dashboard.html', context)
