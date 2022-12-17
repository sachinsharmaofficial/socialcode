from django.urls import path
from Ask_Chat_Get import views

urlpatterns = [
    
    path('', views.index, name = "ask"),
    path('<uuid:ask_id>/', views.ans, name="ans"),
]