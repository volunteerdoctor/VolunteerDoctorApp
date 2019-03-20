from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # ex: /core/
    path('', views.index, name='index'),
    # ex: /core/commitments/
    path('commitments/', views.CommitmentIndexView.as_view(), name='commitments'),
    # ex: /core/commitments/5/
    path('commitments/<int:pk>/', views.CommitmentDetailView.as_view(),
         name='commitment_details'),
    # ex: /core/medics/
    path('medics/',
         views.MedicIndexView.as_view(), name='medics'),
    # ex: /core/commitments/5/
    path('medics/<int:pk>/', views.MedicDetailView.as_view(),
         name='medic_details'),
    # ex: /core/medic/register
    path('register_medic/',
         views.register_medic, name='register_medic'),
    # ex: /core/5/commitments/
    path('<int:medic_id>/commitments/',
         views.medic_commitments, name='medic_commitments'),
    # ex: /core/requests/
    path('requests/', views.RequestIndexView.as_view(), name='requests'),
    # ex: /core/facilities/
    path('facilities/', views.FacilityIndexView.as_view(), name='facilities'),
]
