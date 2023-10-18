from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse
from tablib import Dataset

from .resources import ItemResources





def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        item_resource = ItemResources()
        dataset = item_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response
    return render(request, 'item/export_items.html')




class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ("item_name","description", 'phone_or_email', 'status', 'upload_image')
    template_name = "item/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def save(self):
    #     instance = super(ItemCreateView, self).save()

    #     @transaction.on_commit
    #     def notification_email():
    #         subject = f"A new report at ReportStolenItem.com"
    #         message = f"Read {instance} at ReportStolenItem.com\n\n"
    #         send_mail(subject, message, 'admin@reportstolenitem.com', 'test@email.com', fail_silently=False,)
    #     transaction.on_commit(notification_email)
    #     return instance

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ("item_name","description", 'status', 'upload_image')
    template_name = "item/edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = "item/delete.html"
    success_url = reverse_lazy("item_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# @login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item/list.html', {'items': items})


@login_required
def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item/detail.html', {'item' :item})
