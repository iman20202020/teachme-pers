from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User

from accounts.models import Student, Teacher


class MyUserCreate(UserCreationForm):
    email = forms.EmailField(required=True, label='ایمیل')

    def __init__(self, *args, **kwargs):
        super(MyUserCreate, self).__init__(*args, **kwargs)

        super().__init__(*args, **kwargs)
        for fieldname in ['username',]:
            self.fields[fieldname].help_text = None
    # error_messages = {
    #      'رمز عبور ها یکسان نیست',
    # }
    password1 = forms.CharField(
        label="گذر واژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None,
    )
    password2 = forms.CharField(
        label="تکرار گذر واژه",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',}),
        strip=False,
        help_text=None,
    )
    phone_number = forms.CharField(label="شماره همراه ")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email","phone_number")
        field_classes = {'username': UsernameField}

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','email']

        field_classes = {'username': UsernameField}


class TeacherEditForm(UserChangeForm):
  # class Meta:
    #     model = Teacher
    #
    # password = None
    # points = forms.CharField(label=("your points"),disabled=True)
    # national_id = forms.CharField(label=("National id / PassportNo."))
    # national_card_image = forms.ImageField(label=("National Card/Passport image"), required=False)
   class Meta(UserChangeForm.Meta):
        model = Teacher
        exclude = ['user','email']