from django.test import TestCase
from api.models import Element, Landmark, Entry, IDLandmarks

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

  def testFibula(self):
    fibula = Element.objects.get(bone_name="Fibula")
    fibula_list = fibula.landmark_set.all()
    print(fibula_list)
