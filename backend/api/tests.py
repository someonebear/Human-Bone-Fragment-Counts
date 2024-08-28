from django.test import TestCase
from api.models import Element, Landmark, Entry, IDLandmarks
from django.db.models import RestrictedError
# Create your tests here.

class FibulaTestCase(TestCase):
  def setUp(self):
    Element.objects.create(name="Fibula")
    fibula = Element.objects.get(name="Fibula")
    Landmark.objects.create(name="Head", id="FIB-1", bone=fibula)
    Landmark.objects.create(name="Neck", id="FIB-2", bone=fibula)
    Landmark.objects.create(name="Shaft", id="FIB-3", bone=fibula)
    Landmark.objects.create(name="Distal articular surface", id="FIB-4", bone=fibula)
    Landmark.objects.create(name="Lateral malleolus", id="FIB-5", bone=fibula)

  def test_fibula_elements(self):
    fibula = Element.objects.get(name="Fibula")
    fibula_elements = ["Head", "Neck", "Shaft", "Distal articular surface", "Lateral malleolus"]
    fibula_list = fibula.landmark_set.all()
    for i in fibula_list:
      # Get landmark name out of __str__ method
      landmark_name = str(i).split("-", 1)[0].strip()
      self.assertIn(landmark_name, fibula_elements)

  def test_delete_landmark_cascade(self):
    fibula = Element.objects.get(name="Fibula")
    fibula_list = fibula.landmark_set.all()
    self.assertEqual(fibula_list.count(), 5)
    fibula.delete()
    self.assertEqual(fibula_list.count(), 0)

