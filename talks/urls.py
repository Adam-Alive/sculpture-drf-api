from django.urls import path
from talks import views

urlpatterns = [
    path('talks/', views.TalkList.as_view()),
   ]
