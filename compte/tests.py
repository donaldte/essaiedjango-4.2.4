from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile, User 
from .forms import FromProfile


class TestCaseProfle(TestCase):
    
    def setUp(self):
        
        self.data = {
            'username': 'test',
            "email": 'test@gmail.com',
            "password": 'test1234',
        }
        
        self.user = User.objects.create_user(**self.data)
        
        self.profile = Profile.objects.create(
            user=self.user,
            email=self.user.email,
        )
        
    def test_profile(self):
        self.assertEqual(self.profile.user, self.user)  
        
    
    def test_profile_email(self):
        self.assertEqual(self.profile.email, self.user.email)
        self.data['email'] = 'donald@gmail.com'
        self.assertNotEqual(self.profile.email, self.data['email'])   
        
        
class TestCaseForm(TestCase):
    
    def setUp(self):
        
        self.data = {
            'username': 'test',
            "email": 'test@gmail.com',
            "password": 'test1234',
        }
        
        self.user = User.objects.create_user(**self.data)
        
        
        
        
    def test_valid_form(self):
        
        form = FromProfile(data={'user':self.user, 'email':self.user.email})
        
        self.assertTrue(form.is_valid())
        


class TestCaseAuth(TestCase):
    
    def setUp(self):
        
        self.client = Client()
        
        self.user_data = {
            'username': 'test',
            'password': 'testpassword2',
            'email': 'donaldtedom0@gmail',
        } 
        
        self.user = User.objects.create_user(**self.user_data)                  
        
        
    
    def test_register_view(self):
        
        url = reverse('compte:register') 
        
        response = self.client.get(url) 
        
        self.assertEqual(response.status_code, 200) 
        
        data = {
            'username':'test1',
            'first_name': 'test1',
            'last_name': 'test1',
            'email': 'donaldtedom0@gmail.com',
            'password1': 'test1234',
            'password2': 'test1234',
        }
        
        response = self.client.post(url, data=data)
        
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, reverse('compte:login'), status_code=302)
        
        self.assertTrue(User.objects.filter(username='test1').exists())
        
        
    
    def test_login_view(self):
        
        url = reverse('compte:login')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        user = User.objects.get(username='test')
        
        response = self.client.post(url, {
            'username': 'test',
            'password': 'testpassword2'
        }) 
        
        self.assertEqual(response.status_code, 302) 
        
        self.assertTrue(user.is_authenticated)  
        
        
    def test_logout_view(self):
        
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        
        self.assertTrue(self.client.session['_auth_user_id'])
        url = reverse('compte:logout')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, reverse('compte:login'), 302)
        
        # user = User.objects.get(username=self.user_data['username'])
        
        self.assertNotIn('_auth_user_id', self.client.session)  