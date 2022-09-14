from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class CatalogItemTestCase(TestCase) :
    def setUp(self):
        CatalogItem.objects.create(
            item_name="indomie",
            item_price=3500,
            item_stock=40,
            description="rasa mie goreng ori",
            rating=9,
            item_url="https://www.tokopedia.com/mapstore077/indomie-goreng-1-dus-40-pcs"
        )

    def katalog_sameness(self):
        # Testing if the unit is ok
        indomie = CatalogItem.objects.get(
            item_name="indomie",
            item_price=3500,
            item_stock=40,
            description="rasa mie goreng ori",
            rating=9,
            item_url="https://www.tokopedia.com/mapstore077/indomie-goreng-1-dus-40-pcs"
        )
        # Testing if the functionality is ok
        self.assertEqual(indomie.item_name, "indomie")
        self.assertEqual(indomie.item_price, 3500)
        self.assertEqual(indomie.item_stock, 40)
        self.assertEqual(indomie.description, "rasa mie goreng ori")
        self.assertEqual(indomie.rating, 9)
        self.assertEqual(indomie.item_url, "https://www.tokopedia.com/mapstore077/indomie-goreng-1-dus-40-pcs")