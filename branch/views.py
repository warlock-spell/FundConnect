from django.shortcuts import render, redirect, get_object_or_404
from .forms import BranchForm, EditBranchForm
from .models import Branch


# Create your views here.

def home(request):
    return render(request, 'branch/home.html')


def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch:branch-edit')
    else:
        form = BranchForm()

    return render(request, 'branch/create-branch.html', {'form': form})


def list_branch(request):
    branches = Branch.objects.all()
    context = {
        'branches': branches,
    }
    return render(request, 'branch/list-branches.html', context)


# not in use
# but kept for reference
def detail_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    context = {
        'branch': branch,
    }
    return render(request, 'branch/detail-branch.html', context)


def edit_selected_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)

    if request.method == 'POST':
        form = EditBranchForm(request.POST, instance=branch)

        if form.is_valid():
            form.save()

            return redirect('branch:branch-edit')
    else:
        form = EditBranchForm(instance=branch)

    return render(request, 'branch/edit-branch-pk.html', {
        'form': form,
        'title': 'Edit branch',
    })


def edit_branch(request):
    branches = Branch.objects.all()
    context = {
        'branches': branches,
    }
    return render(request, 'branch/edit-branch.html', context)


def remove_branch(request):
    return render(request, 'branch/remove-branch.html')
