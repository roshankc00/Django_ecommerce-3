
from django.urls import path,include
from .views import CategoryView

# register StudentViewset with Router 


urlpatterns = [
    path('categories/',CategoryView.as_view(),name="get All categories"),
    path('categories/<int:pk>/',CategoryView.as_view(),name="getSingleCategory")
]
