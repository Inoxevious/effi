from django.urls import path, include # new

from .views import HomePageView, SearchResultsView,  search_detail
app_name = 'search'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search'),
    # path('<int:plant_id>/search_detail/', search_detail, name='search_detail'),
    path('<int:hotspot_id>/search_detail/', search_detail, name='search_detail'),
    path('', HomePageView.as_view(), name='home'),
]