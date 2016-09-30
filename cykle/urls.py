from django.conf.urls import url
from cykle import views
#добавлять сюда метод открытия страниц
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^lab2/$',views.LabPageView.as_view()),
    url(r'^lab3/$', views.LabPageView.as_view())
]