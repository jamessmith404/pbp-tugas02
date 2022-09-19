# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist, show_watchlist_html, show_watchlist_xml, show_watchlist_json #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json_by_id, show_xml_by_id #sesuaikan dengan nama fungsi yang dibuat

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_watchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_watchlist_xml, name="show_mywatchlist_xml"), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_watchlist_json, name="show_mywatchlist_json"), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name="show_xml_by_id"), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_json_by_id, name="show_json_by_id"), #sesuaikan dengan nama fungsi yang dibuat
]