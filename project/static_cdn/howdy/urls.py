from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
	url(r'^aboutus/$',views.AboutPageView.as_view()),
]
      