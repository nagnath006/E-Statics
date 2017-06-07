from django.conf.urls import url,include
from howdy import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.HomePageView.as_view()),
	url(r'^aboutus/$',views.AboutPageView.as_view()),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),


]
      