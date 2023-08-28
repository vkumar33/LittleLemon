from django.urls import path
#from .views import menuview, bookingview
from . import views

urlpatterns = [
    #path('menu/', menuview.as_view()),
    #path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),      
]
