from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = (
        'name',
        'email',
        'subject',
        'content'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'content',
            Submit('submit', 'Send Message', css_class='button button-a button-big button-rouded')
        )
