from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
)


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text ='Required. Format: YYYY-MM-DD',
                                 widget = forms.TextInput
                                 (attrs =
                                 {'placeholder' : 'DOB',
                                 'class' : 'form-control',
                                 'style' : 'width:200px'}
                                  ))
    gender = forms.ChoiceField(choices = GENDER,
                               required = True,
                               widget=forms.Select
                               (attrs =
                               {'class' : 'dropdown-item',
                                'style' : 'width:200px'}))
    address = forms.CharField(required = True,
                              widget = forms.TextInput(attrs =
                              {'placeholder' : 'Address',
                               'class' : 'form-control',
                               'style' : 'width:200px'}))
    city = forms.CharField(required = True,
                           widget = forms.TextInput(attrs =
                           {'placeholder' : 'City',
                            'class' : 'form-control',
                            'style' : 'width:200px'}))
    pincode = forms.IntegerField(required = True,
                                 max_value = 999999,
                                 widget = forms.NumberInput(attrs =
                                 {'placeholder' : 'Pincode',
                                  'class' : 'form-control',
                                  'style' : 'width:200px'}))
    email = forms.EmailField(required = True,
                             widget = forms.EmailInput(attrs=
                             {'placeholder' : 'E-Mail',
                              'class' : 'form-control',
                              'style' : 'width:200px'}))
    mobile_number = forms.IntegerField(required = True,
                                       max_value = 9999999999,
                                       widget = forms.NumberInput(attrs =
                                       {'placeholder' : 'Mobile Number',
                                        'class' : 'form-control',
                                        'style' : 'width:200px'}))
    state = forms.CharField(required = True,
                            widget = forms.TextInput(attrs =
                            {'placeholder' : 'State',
                             'class' : 'form-control',
                             'style' : 'width:200px'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs =
                               {'placeholder' : 'Password',
                                'class' : 'form-control',
                                'style' : 'width:200px'}),
                                label = "Password",
                                required = True)
    password2 = forms.CharField(widget = forms.PasswordInput(attrs =
                               {'placeholder' : 'Confirm Password',
                                'class' : 'form-control',
                                'style' : 'width:200px'}),
                                label = "Confirm Password",
                                required = True)
    username = forms.CharField(widget = forms.TextInput(attrs =
                              {'placeholder' : 'Username',
                               'class' : 'form-control',
                               'style' : 'width:200px'}),
                               label = "Username",
                               required = True)
    first_name = forms.CharField(required = True,
                                 widget = forms.TextInput(attrs =
                                 {'placeholder' : 'First Name',
                                  'class' : 'form-control',
                                  'style' : 'width:200px'}))
    last_name = forms.CharField(required = False,
                                widget = forms.TextInput(attrs =
                                {'placeholder' : 'Last Name',
                                 'class' : 'form-control',
                                 'style' : 'width:200px'}))
    profile_pic = forms.FileField(required = False)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'address',
                  'city',
                  'pincode',
                  'state',
                  'mobile_number',
                  'email',
                  'profile_pic',
                  'password1',
                  'password2',
                  )
