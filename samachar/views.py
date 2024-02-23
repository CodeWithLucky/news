from django.shortcuts import redirect, render
from django.views import View
from . import news_api

from samachar.forms import NewsForm
from samachar.models import NewsModel

# Create your views here
class YourView(View):
    def get(self, request):
        data = NewsModel.objects.all()
        form = NewsForm()
        return render(request,'index.html', {'form':form, 'data' : data})
    def add_news(request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return redirect('index')
        return render(request, 'insert.html',{'form':news_form})
    
    def detail(request, id):
        data = NewsModel.objects.filter(id=id)
        return render(request, 'detail.html', {'data' : data})
    
