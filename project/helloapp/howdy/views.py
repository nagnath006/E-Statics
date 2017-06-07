from django.shortcuts import render
from django.views.generic import TemplateView

#737432306620-33k73m2lin46mc9trpqg513eh3uo3h0c.apps.googleusercontent.com

# Create your views here.

def home(request):
   return render(request, 'home.html', {'user': request.user,'request': request,})
class HomePageView(TemplateView):
      def get(self,request,**kwargs):
	      return render(request,'index.html',context = None)
class AboutPageView(TemplateView):
      template_name = "aboutus.html"
      
     