from django.test import TestCase
from .models import Employee,Profession

# Create your tests here.

class NumberEqual(TestCase):
   
   def setUp(self):
      print("\n NumberEqual setup successfuly")
      
   def test_equal(self):
      print('\ntesting start test_equal ')
      
      res = self.assertEqual(1, 1)
      print(f'\n Test Output is: {res}')
      return res
   
class ProfessionModelCase(TestCase):
   
   def setUp(self):
      print('\n Default setup ProfessionModelCase ')
   
   def test_create_data(self):
      print('\ntesting start test_create_data ')
      
      prof_name = ['abc', 'def', 'computer', 'mechanical']
      
      for i in range(len(prof_name)):
         prof = prof_name[i]
         print(prof)
         # obj creation
         obj = Profession.objects.create(name=prof)
          
          # checking  profession name is equal to name or not
         (self.assertEquals(obj.name, prof))
         
      professions = Profession.objects.all().count()
      print(professions+1, len(prof_name))
      self.assertEquals(4, 5)
   


      