from django.shortcuts import render
from django.http import JsonResponse
from .models import PageData
import requests
# Create your views here.
def search_page(request):
    return render(request, 'index.html')

def fetch_using_url(url):
    response = requests.get(url).text
    desc = response.split("<title>")[1].split("</title>")[0]
    price = response.split(">₹")[1].split("<")[0].replace(",","")
    PageData.objects.create(url=url, desc=desc, price=price)
    return {'url': url, 'desc': desc, 'price': price}

def send_data(request):
    fields = ['url', 'desc', 'price']
    if request.POST:
        url = request.POST.get('url')
        try:
            data = PageData.objects.filter(url=url).latest('created_on')
        except:
            data = fetch_using_url(url)
        else:
            data = { i: data.__dict__[i] for i in data.__dict__ if i in fields }
        return JsonResponse(data)
    return JsonResponse({'status': 'Expecting a POST Request'})
