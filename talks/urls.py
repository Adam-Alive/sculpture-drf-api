from django.urls import path
from talks import views

urlpatterns = [
    path('talks/', views.TalkList.as_view()),
    path('talks/<int:pk>/', views.TalkDetail.as_view()),
   ]
