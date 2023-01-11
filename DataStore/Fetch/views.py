from django.shortcuts import render
from django.http import JsonResponse
from .models import PageData
# Create your views here.
def search_page(request):
    return render(request, 'index.html')

def send_data(request):
    fields = ['url', 'desc', 'price']
    if request.POST:
        url = request.POST.get('url')
        try:
            data = PageData.objects.filter(url=url).latest('updated_on')
        except:
            """Need to fetch from internet and update user and models accordingly"""
            data = {'status': 'Under Construction'}
        else:
            data = { i: data.__dict__[i] for i in data.__dict if i in fields }
        return JsonResponse(data)
    return JsonResponse({'status': 'Expecting a POST Request'})
