from django.forms import ModelForm, Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        """Определяем модель на основе которой создаем форму"""
        model = Contact
        """Поля которые будут использоваться для заполнения"""
        fields = ['parents_name', 'child_name', 'age',
                  'phone_number', 'hall', 'coach_name']

#   def __init__(self, *args, **kwargs):
#        super(ContactForm, self).__init__(*args, **kwargs)
#        self.fields['parents_name'].widget.attrs.update({'class ': 'popup'})
#        self.fields['child_name'].widget.attrs.update({'class ': 'popup'})
