from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):
    def test_watchlist_html(self):
        client = Client() # Objek client yang membuka browser
        response = client.get(reverse('mywatchlist:show_mywatchlist_html'))

        self.assertEquals(response.status_code, 200) # Check apakah template mengembalikan response code yang benar
        self.assertTemplateUsed(response, 'base.html') # Check apakah template menggunakan layout base.html
    
    def test_watchlist_json(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_mywatchlist_json'))

        self.assertEquals(response.status_code, 200)

    def test_watchlist_xml(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_mywatchlist_xml'))

        self.assertEquals(response.status_code, 200)
