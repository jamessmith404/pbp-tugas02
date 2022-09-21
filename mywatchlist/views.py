from multiprocessing import context
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse # from lab02 docs
from django.core import serializers

# Create your views here. Tugas 3 PBP
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    watched = MyWatchList.objects.filter(watched=True).count()
    not_watched = MyWatchList.objects.filter(watched=False).count()
    context = {
        'list_watchlist': data_mywatchlist,
        'is_watchlist': True if watched >= not_watched else False,
        'nama': 'James Smith Wigglesworth',
        'NPM': '2106750225',
    }
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_watchlist_html(request):
    data = MyWatchList.objects.all()

    context = {
        'list_watchlist': data,
        'nama': 'James Smith Wigglesworth',
        'NPM': '2106750225',
    }
    return render(request, "mywatchlist.html", context)

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")