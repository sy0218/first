from urllib import request
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

class HomeView(TemplateView):
    template_name = 'home.html'
    
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    Permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj =self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


def cumtomAPI_TV(request):
    req = requests.get('https://finance.naver.com//marketindex/exchangeList.naver')
    soup = BeautifulSoup(req.text, 'html.parser')
    
    country_set = soup.select('table tbody tr:nth-child(-n+14) .tit a')
    price_set = soup.select('table tbody tr:nth-child(-n+14) .sale')
        
    country_Arr = []
    for country in country_set:
        country_Arr.append(country.string.replace("\n", "").replace('\t',''))
        
    price_Arr = []
    for price in price_set:
        price_Arr.append(price.string.replace("\n", "").replace('\t',''))

    key = 'LU10B4YcmjsCI3uZN3q0+dsSE60qU7AnQEZUHv2rYjsA7VkxxjWC1lELnvBA6EHcGY4o4fF2i9lNKbCHmuNZZA=='
    url = 'http://apis.data.go.kr/B551177/PaxFltSched/getPaxFltSchedDepartures'
    params = {'serviceKey' : 'LU10B4YcmjsCI3uZN3q0+dsSE60qU7AnQEZUHv2rYjsA7VkxxjWC1lELnvBA6EHcGY4o4fF2i9lNKbCHmuNZZA==', 'numOfRows' : '10', 'pageNo' : '1', 'lang' : 'K', 'airport' : 'NRT', 'type' : 'json' }

    response = requests.get(url, params=params)
    result = response.content.decode('utf8').replace("'", '"')
    
    print(result)
    import json

    context={}
    test1 = country_Arr + price_Arr
    context["object_list"] = zip(country_Arr, price_Arr)
    context["object_list2"] =  json.loads(result)
    return render(request, "movie_page.html", context)

        


    key = 'LU10B4YcmjsCI3uZN3q0+dsSE60qU7AnQEZUHv2rYjsA7VkxxjWC1lELnvBA6EHcGY4o4fF2i9lNKbCHmuNZZA=='
    url = 'http://apis.data.go.kr/B551177/PaxFltSched/getPaxFltSchedDepartures'
    params = {'serviceKey' : 'LU10B4YcmjsCI3uZN3q0+dsSE60qU7AnQEZUHv2rYjsA7VkxxjWC1lELnvBA6EHcGY4o4fF2i9lNKbCHmuNZZA==', 'numOfRows' : '10', 'pageNo' : '1', 'lang' : 'K', 'airport' : 'NRT', 'type' : 'json' }

    response = requests.get(url, params=params)
    print(response.content)
    import json

    context = super().get_context_data(**kwargs)
    context["result"] = json.loads(response.text)
    return context




        




