from django.test import TestCase
from api.models import Element, Landmark, Entry, IDLandmarks
from django.db.models import RestrictedError
# Create your tests here.

class FibulaTestCase(TestCase):
  def setUp(self):
    Element.objects.create(bone_name="Fibula")
    fibula = Element.objects.get(bone_name="Fibula")
    Landmark.objects.create(landmark_name="Head", bone=fibula)
    Landmark.objects.create(landmark_name="Neck", bone=fibula)
    Landmark.objects.create(landmark_name="Shaft", bone=fibula)
    Landmark.objects.create(landmark_name="Distal articular surface", bone=fibula)
    Landmark.objects.create(landmark_name="Lateral malleolus", bone=fibula)

  def test_fibula_elements(self):
    fibula = Element.objects.get(bone_name="Fibula")
    fibula_elements = ["Head", "Neck", "Shaft", "Distal articular surface", "Lateral malleolus"]
    fibula_list = fibula.landmark_set.all()
    for i in fibula_list:
      self.assertIn(str(i), fibula_elements)

  def test_delete_landmark_cascade(self):
    fibula = Element.objects.get(bone_name="Fibula")
    fibula_list = fibula.landmark_set.all()
    self.assertEqual(fibula_list.count(), 5)
    fibula.delete()
    self.assertEqual(fibula_list.count(), 0)

