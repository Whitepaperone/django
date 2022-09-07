from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Travel
from .forms import TravelForm

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    travels = Travel.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = TravelForm(request.POST)
        if form.is_valid():
            traveli = form.save()
            return redirect('travels:detail', traveli.pk)
    else:
        # new
        form = TravelForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)


@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    travel = Travel.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)


@require_POST
def delete(request, pk):
    travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    travel = Travel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        # form = travelForm(data=request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {
        'travel': travel,
        'form': form,
    }
    return render(request, 'travels/update.html', context)
