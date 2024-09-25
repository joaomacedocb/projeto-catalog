from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, DeleteView

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
    
        if search:
            cars = cars.filter(model__icontains=search).order_by('model')

        return render(
            request,
            'cars.html',
            {'cars': cars}
        )

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
class ItemDetailView(DetailView):
    model = Car
    template_name = 'item_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ItemUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'item_update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('item_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class ItemDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = '/cars/'
