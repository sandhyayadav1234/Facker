from django.urls import path
from . import views
urlpatterns = [
    path('fc/',views.fackerView,name='faker'),
    path('dv/',views.DisplayView,name='show'),
    path('uv/<int:f_roll>',views.UpdateView,name='update'),
    path('dvv/<int:f_roll>',views.DeleteView,name='delete'),
    path('m_d/',views.mul_chk,name='multi_chk'),
    ]