from django import forms
#import settings
from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    name = forms.CharField()
    phonenumber = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'onkeydown' : "checkContentLimit('id_content', 500)",
                                                           'onkeyup': "checkContentLimit('id_content',500)",
                                                           'onchange': "checkContentLimit('id_content',500)",
                                                           }))
    receive_a_copy_of_message = forms.BooleanField(required=False)

  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
