from django.urls import path

from . import views

urlpatterns = [
    # ex: /core/
    path('', views.index, name='index'),
    # ex: /core/commitments/5/
    path('commitments/<int:commitment_id>/', views.commitment_details,
         name='commitment_details'),
    # ex: /core/commitments/
    path('commitments/',
         views.commitments, name='commitments'),
    # ex: /core/5/commitments/
    path('<int:doctor_id>/commitments/',
         views.doctor_commitments, name='doctor_commitments'),
]
