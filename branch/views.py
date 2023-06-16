from django.shortcuts import render, redirect, get_object_or_404
from .forms import BranchForm, EditBranchForm
from .models import Branch
from member.models import Member
from dashboard.models import Controller


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


def remittance_form_view(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')

        branches = Branch.objects.all()
        controller = Controller.objects.all().first()
        members = Member.objects.all()
        members = members.filter(active_user=True)

        # Calculations

        loan_emi = {}
        loan_interest = {}

        for member in members:
            # add loan emi and key is id
            loan_emi[member.id] = round(member.loan / 12, 2)  # will change later
            loan_interest[member.id] = round(member.loan * (
                    controller.loan_interest / 100),
                                             2)  # will change later, according to controller.loan_interest_period

        context = {
            'month': month,
            'year': year,
            'branches': branches,
            'members': members,
            'controller': controller,
            'loan_emi': loan_emi,
            'loan_interest': loan_interest,
        }

        return render(request, 'branch/remittance-template.html', context)

    return render(request, 'branch/remittance-form.html')
