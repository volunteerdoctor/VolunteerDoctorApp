from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Medic, Commitment, Request, Facility


def index(request):
    return render(request, 'index.html')


class CommitmentIndexView(generic.ListView):
    template_name = 'commitment/index.html'
    context_object_name = 'commitments'

    def get_queryset(self):
        """Return commitments."""
        return Commitment.objects.order_by('-created_at')


class CommitmentDetailView(generic.DetailView):
    model = Commitment
    template_name = 'commitment/detail.html'


def medic_commitments(request, medic_id):
    commitments = get_object_or_404(Commitment, medic=medic_id)
    context = {'commitments': commitments}
    return render(request, 'commitment/index.html', context)


class MedicIndexView(generic.ListView):
    template_name = 'medic/index.html'
    context_object_name = 'medics'

    def get_queryset(self):
        """Return medics."""
        return Medic.objects.order_by('first_name')


class MedicDetailView(generic.DetailView):
    model = Medic
    template_name = 'medic/detail.html'


def register_medic(request):
    return render(request, 'medic/register.html')


def register_commitment(request, medic_id):
    commitment = Commitment.get(pk=request.POST['choice'])
    commitment.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('commitment_details', args=(commitment.id,)))


class RequestIndexView(generic.ListView):
    template_name = 'request/index.html'
    context_object_name = 'requests'

    def get_queryset(self):
        """Return requests."""
        return Request.objects.order_by('-created_at')


class FacilityIndexView(generic.ListView):
    template_name = 'facility/index.html'
    context_object_name = 'requests'

    def get_queryset(self):
        """Return facilities."""
        return Facility.objects.order_by('name')
