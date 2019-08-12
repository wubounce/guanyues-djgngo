from django.shortcuts import render
from django.views.generic.base import View  # 类方法展示view
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from product.models import ProductSeries, Product
from .models import Company


class CompanyView(View):
    def get(self, request):
        all_series = ProductSeries.objects.all()
        seriers_id = '1'
        all_products = Product.objects.filter(product_series_id=int(seriers_id))[:6]
        all_company = Company.objects.all()

        return render(request, 'index.html', {
            'all_series': all_series,
            'all_products': all_products,
            'seriers_id': seriers_id,
            'all_company':all_company
        })