from django import forms
from e_mailer.models import Mail


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = '__all__'