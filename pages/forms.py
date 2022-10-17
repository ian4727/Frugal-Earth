from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Room, User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host']
        
class UserForm(ModelForm):
        class Meta:
            model = User
            fields = ['name', 'username', 'email', 'avatar']
            
