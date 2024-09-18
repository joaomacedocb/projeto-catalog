from django import forms
from django.core.exceptions import ValidationError
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200, label='Modelo')
    brand = forms.ModelChoiceField(Brand.objects.all(),label='Marca')
    factory_year = forms.IntegerField(label='Ano de fabricação')
    model_year = forms.IntegerField(label='Ano do modelo')
    plate = forms.CharField(max_length=7, label='Placa')
    value = forms.FloatField(label='Preço')
    photo = forms.ImageField(label='Foto')

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factoryYear = self.cleaned_data['factory_year'],
            modelYear = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'factoryYear', 'modelYear', 'plate', 'value', 'photo']
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factoryYear': 'Ano de Fabricação',
            'modelYear': 'Ano do Modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Foto',
        }   

    def clean_factoryYear(self):
        factoryYear = self.cleaned_data.get('factoryYear')
        if factoryYear < 1970:
            self.add_error('factoryYear', 'Erro: Só são permitidos veículos a partir de 1970.')
        return factoryYear
    
    def clean(self):
        cleaned_data = super().clean()
        factoryYear = cleaned_data.get('factoryYear')
        modelYear = cleaned_data.get('modelYear')

        if modelYear < factoryYear:
            raise ValidationError("Erro: O ano do modelo não pode ser menor do que o ano de fabricação.")
        return cleaned_data