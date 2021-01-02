from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/', views.create_card, name='create_card'),
    path('edit/<int:id>/', views.edit_card, name='edit_card'),
    path('card/delete/<int:id>/', views.delete_card, name='delete_card')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
