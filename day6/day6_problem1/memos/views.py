from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Memo
from .forms import MemoForm

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    memos = Memo.objects.all()
    context = {
        'memos': memos,
    }
    return render(request, 'memos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = MemoForm(request.POST)
        if form.is_valid():
            memoi = form.save()
            return redirect('memos:detail', memoi.pk)
    else:
        # new
        form = MemoForm()
    context = {
        'form': form,
    }
    return render(request, 'memos/create.html', context)


@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo,
    }
    return render(request, 'memos/detail.html', context)


@require_POST
def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    memo = Memo.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        # form = MemoForm(data=request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memos:detail', memo.pk)
    else:
        form = MemoForm(instance=memo)
    context = {
        'memo': memo,
        'form': form,
    }
    return render(request, 'memos/update.html', context)
