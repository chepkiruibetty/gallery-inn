from django.test import TestCase

# Create your tests here.from django.test import TestCase
from .models import Images,Category,Location


# Create your tests here.


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.zuri = Location(locs_name='zuri')
        self.flowers = Category(name='general')
        self.image = Image(image='media/rose.jpeg',image_name='rose', image_descprition='best gift you can give to lover',location=self.zuri,category=self.flowers, id=1)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    # Testing Save Method

    def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name = 'flowers', id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

    def test_save_method(self):
        self.category.save_category()
        cate = Category.objects.all()
        self.assertTrue(len(cate)>0)
        
    def test_delete_method(self):
        self.category.delete_category
        cate = Category.objects.all()
        self.assertTrue(len(cate) is 0)
        
    def test_display_all(self):
        flowers = Category(name='general')
        flowers.save_category()
        one = Category.objects.all()
        print(len(one))
        self.assertTrue(len(one),2)
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.zuri = Location(locs_name = 'zuri', id=1)
        
        
    #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.zuri,Location)) 

    def test_save_method(self):
        self.zuri.save_locs()
        images = Location.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_method(self):
        self.zuri.delete_locs()
        locations = Location.objects.all()
        self.assertTrue(len(locations) is 0)
        
    def test_display_all(self):
        rose= Location(loc_name='zuri')
        rose.save_loc()
        self.zuri.save_loc()
        locations = Location.objects.all()
        print(len(locations))
        self.assertTrue(len(locations),2)

        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        


    