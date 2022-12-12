from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#<<<<<<< HEAD
from .models import Room, User, Report
#=======
from .models import Room, User
#>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
#<<<<<<< HEAD
        exclude = ['host', 'price']

#=======
        exclude = ['host']
        
#>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
class UserForm(ModelForm):
        class Meta:
            model = User
            fields = ['name', 'username', 'email', 'avatar']
#<<<<<<< HEAD


class ReportForm(ModelForm):
        class Meta:
            model = Report
            fields = '__all__'
            exclude = ['user']


#=======
            
#>>>>>>> 840bf37d3ca46419406fb7ae06d5a6d9ec637024
