from OrderRepository import *
import unittest

rep = None

good1 = Good(1,"apple", 10)
good2 = Good(2,"pineaplle", 50)
good3 = Good(3,"limon", 15)
good4 = Good(4,"mango", 60)
good5 = Good(5,"orange", 25)

order1 = Order(1, 1, [good1])
order2 = Order(2, 5, [good1, good2])
order3 = Order(3, 3, [good1, good2, good3])
order4 = Order(4, 2, [good1, good2, good3, good4])
order5 = Order(5, 4, [good1, good2, good3, good4, good5])

rep = OrderRepository()

rep.add(order1)
rep.add(order2)
rep.add(order3)
rep.add(order4)
rep.add(order5)

# for i in rep.list():
#     print(i)
class Tests(unittest.TestCase):
    def setUp(self):
        self.rep = None
        self.rep1 = None

    def test_add(self):  
        self.rep1 = None
        self.rep1 = OrderRepository()
        self.rep1.add(order1)
        self.rep1.add(order2)
        self.rep1.add(order3)
        self.rep1.add(order4)
        self.rep1.add(order5)
        self.assertEqual(self.rep1.orders, [order1, order2, order3, order4, order5])

    def test_del(self):
        self.rep = rep
        self.rep.delete(5)
        self.assertEqual(self.rep.orders, [order1, order2, order3, order4])
 
    def test_get(self):
        self.rep = rep
        self.assertEqual(order3, self.rep.get(3))


    def test_list3(self):
        self.rep = rep
        self.assertEqual(self.rep.list(2), [order3, order4])

    def test_listnone(self):
        self.rep = rep
        self.assertEqual(self.rep.list(), [order1, order2, order3, order4]) 


if __name__ == '__main__':  
    unittest.main()
    