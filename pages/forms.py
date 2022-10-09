from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Room

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        