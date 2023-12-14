from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse, Http404

import os

from solution.settings import MEDIA_ROOT, BASE_DIR
from .models import Font
from .forms import TickerCreateForm


def download(request, pk):
    file_path = str(BASE_DIR / MEDIA_ROOT) + '/ticker_' + str(pk) + '.mp4'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/mp4")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

class TickerCreateView(FormView):
    form_class = TickerCreateForm
    template_name = 'ticker/create_ticker.html'

    def form_valid(self, form):
        ticker_pk = form.create_ticker()
        return redirect(reverse_lazy('download_ticker', kwargs={'pk':ticker_pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create ticker'
        return context


class FontCreateView(CreateView):
    model = Font
    template_name = 'ticker/create_font.html'
    fields = '__all__'
    success_url = reverse_lazy('create_ticker')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create font'
        return context