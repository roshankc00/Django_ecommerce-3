
from django.urls import path,include
from .views import CategoryView,ProductView

# register StudentViewset with Router 


urlpatterns = [
    path('categories/',CategoryView.as_view(),name="get All categories"),
    path('categories/<int:pk>/',CategoryView.as_view(),name="getSingleCategory"),
    path('',ProductView.as_view(),name="get All categories"),
    path('<int:pk>/',ProductView.as_view(),name="getSingleCategory"),
]
