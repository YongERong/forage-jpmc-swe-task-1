import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    """ ------------ getDataPoint ------------ """
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  
  """ ------------ getRatio ------------ """
  def test_getRatio_calculateRatio(self):
     cases = [
        [119.2, 120.48],
        [121.68, 117.87]
     ]
     for price_a, price_b in cases:
        self.assertEqual(getRatio(price_a, price_b), price_a/price_b)
  
  def test_getRatio_calculateRatioPriceAIsZero(self):
     cases = [
        [0, 120.48],
        [0, 117.87]
     ]
     for price_a, price_b in cases:
        self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_calculateRatioPriceBIsZero(self):
     cases = [
        [119.2, 0],
        [121.68, 0]
     ]
     for price_a, price_b in cases:
        self.assertEqual(getRatio(price_a, price_b), None)

if __name__ == '__main__':
    unittest.main()
