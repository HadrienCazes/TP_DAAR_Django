from django.urls import path
from mytig import views

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('shipPoints/', views.RedirectionShipPointsList.as_view()),
    path('shipPoint/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('availableProduct/<int:pk>/', views.DisponibleDetail.as_view()),
    path('availableProducts/', views.DisponibleList.as_view()),
]
