from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from processor.models import (
Business, CapitalInvestmentRequirements, MarketAnalysis, Risk, CapitalInvestmentRequirementsItem, GeneralCosts, DirectCosts, DirectCostsItem, ProjectProductCostPriceStructure, ProductionOperatingCosts
)
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from hotspot.models import  Hotspot, ActiveHotspot
import csv
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify



def search_detail(request,hotspot_id):
        totaldict = {}
        price_structure_total = float()
        desiel_pump_pricedict = {}
        petrol_pump_pricedict = {}
        addressdict = {}
        gas_pump_pricedict = {}
        price = float()
        hotspot = Hotspot.objects.get(id=hotspot_id)
        id = hotspot.id
        try:
                cpr = ActiveHotspot.objects.get(hotspot_id=id) 
                print('active hot spot found ',cpr.id, ' ___', cpr.desiel_pump_price)
                desiel_pump_pricedict[cpr.id] = []
                gas_pump_pricedict[cpr.id] = []
                petrol_pump_pricedict[cpr.id] = []
                desiel_pump_pricedict[cpr.id].append(cpr.desiel_pump_price)
                gas_pump_pricedict[cpr.id].append(cpr.gas_pump_price)
                petrol_pump_pricedict[cpr.id].append(cpr.petrol_pump_price)


        except (TypeError, ValueError, OverflowError, Hotspot.DoesNotExist):
                        error_message = 'Data  not added yet'

        
        context = {
                'name': hotspot.reference,
                'city': hotspot.city,
                'hotspot': hotspot,
                'desiel_pump_pricedict': desiel_pump_pricedict,
                'gas_pump_pricedict': gas_pump_pricedict,
                'petrol_pump_pricedict': petrol_pump_pricedict,
        }
        return render(request, 'pages/hotspot_detail.html', context )

class HomePageView(TemplateView):
    template_name = 'cities/home.html'


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

class SearchResultsView(ListView):
   
    template_name = 'pages/search_result.html'

    

    # queryset = City.objects.filter(name__icontains='Gweru')

    def get_queryset(self, **kwargs):
        
        text_query = self.request.GET.get('q')
        city_query = self.request.GET.get('q')
        province_query = self.request.GET.get('q')
        fuel_type_query = self.request.GET.get('q')
        production_type_query = self.request.GET.get('q')
        labour_query = self.request.GET.get('q')
        year_return_query = self.request.GET.get('q')


#To execute a more complex query we have to use three new Django objects: 
# SearchVector, SearchQuery, SearchRank  from postgres contrib
        search_query = SearchQuery(text_query) & SearchQuery(city_query) | SearchQuery(fuel_type_query)
        search_vector = SearchVector('reference', weight='A' ) + SearchVector('current_volume', weight='B')
        search_rank = SearchRank(search_vector, search_query)
        trigram_similarity = TrigramSimilarity('reference', text_query)

#Ranking Searches
        global object_list, paged_object_list
        object_list = Hotspot.objects.annotate(
             rank=search_rank 
            ).order_by(
            '-rank'
            )
        print('objet found',object_list)


        paginator = Paginator(object_list,3)
        page = self.request.GET.get('page')
        paged_object_list = paginator.get_page(page)


        return paged_object_list


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        total = dict()
        cap_item = []
        address = []
        desiel_pump_pricedict = {}
        petrol_pump_pricedict = {}
        addressdict = {}
        gas_pump_pricedict = {}
        business = paged_object_list
        print('hot spot',business)
        price = float()
        for a in business:
                try:
                        cpr = ActiveHotspot.objects.get(hotspot_id=a.id) 
                        print('active hot spot found ',cpr.id, ' ___', cpr.desiel_pump_price)
                        desiel_pump_pricedict[cpr.id] = []
                        gas_pump_pricedict[cpr.id] = []
                        petrol_pump_pricedict[cpr.id] = []
                        desiel_pump_pricedict[cpr.id].append(cpr.desiel_pump_price)
                        gas_pump_pricedict[cpr.id].append(cpr.gas_pump_price)
                        petrol_pump_pricedict[cpr.id].append(cpr.petrol_pump_price)
                except (TypeError, ValueError, OverflowError, ActiveHotspot.DoesNotExist):
                        dcost = 'Risk not added yet'       


        for b in business:
                addressdict[b.id] = []
                address = 'Zimbabwe' + ' ' + str(b.city) + ' ' +  str(b.neigbhourhood) + ' ' + str(b.residence)
                addressdict[b.id].append(address)
                print("ADRESS addressdict ", addressdict)
        context['addressdict'] = addressdict
        print('active hot spot found desiel_pump_pricedict ',desiel_pump_pricedict) 
        context['desiel_pump_pricedict'] = desiel_pump_pricedict
        context['gas_pump_pricedict'] = gas_pump_pricedict
        context['petrol_pump_pricedict'] = petrol_pump_pricedict


        return context


