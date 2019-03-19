from django.shortcuts import get_object_or_404, render
from .models import Commitment


def index(request):
    return render('index')


def commitment_details(request, commitment_id):
    commitment = get_object_or_404(Commitment, pk=commitment_id)
    context = {'commitment': commitment}
    return render(request, 'commitment/details.html', context)


def commitments(request):
    commitments = Commitment.objects.order_by('-created_at')
    context = {'commitments': commitments}
    return render(request, 'commitment/index.html', context)


def doctor_commitments(request, doctor_id):
    return render('doctor.commitments')


def signup(request):
    return render('doctor.signup')
