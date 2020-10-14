from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
from account.models import AccountUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def individual(request, user_id):
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    print(user.profile_pic)

    extra_context = extra_context or {"user":user}
    return render(request, 'hotspotdash/home.html', extra_context )

def home(request):
    return render(request, 'hotspotdash/home.html' )

def profile_info(request):
    return render(request, 'farmer/profile.html' )
