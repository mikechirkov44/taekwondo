from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        """Определяем модель на основе которой создаем форму"""
        model = Contact
        """Поля которые будут использоваться для заполнения"""
        fields = ['parents_name', 'child_name',
                  'coach_name', 'hall', 'age', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['parents_name'].widget.attrs.update(
            {'placeholder': 'ФИО родителя'})
        self.fields['child_name'].widget.attrs.update(
            {'placeholder': 'ФИО ребенка'})
        self.fields['coach_name'].widget.attrs.update(
            {'placeholder': 'Тренер'})
        self.fields['hall'].widget.attrs.update(
            {'placeholder': 'Спортивный зал'})
        self.fields['age'].widget.attrs.update(
            {'placeholder': 'Возраст ребенка'})
        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Номер телефона'})
