from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Last Name")
#     return value


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False, label='First Namae', help_text="Enter characters only")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100, validators=[validate_comma])

#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid First Name")
#         return data

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # fields = ['first_name','last_name','email']
        fields= '__all__'
        # exclude=('first_name',)
        labels = {
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        # help_texts = {'first_name': _('Enter Character Only')}
        error_messages={
            'first_name' : {
                'required' : _('you cannot move forward without first name')
            } 
        }
