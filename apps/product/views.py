from django.shortcuts import render
from django.views.generic.base import View  # 类方法展示view
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import ProductSeries, Product


class ProductListView(View):
    def get(self, request, seriers_id):
        all_series = ProductSeries.objects.all()
        all_products = Product.objects.filter(product_series_id= int(seriers_id))
        # 对产品进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_products, 6, request=request)

        products = p.page(page)

        return render(request, 'product.html', {
            'all_series': all_series,
            'products': products,
            'seriers_id': seriers_id
        })


class DetailView(View):
    def get(self, request):
        product_id = request.GET.get('product', '')
        seriers_id = request.GET.get('series', '')
        all_series = ProductSeries.objects.all()
        product = Product.objects.get(id=int(product_id))
        return render(request, 'product_detail.html',{
            'all_series': all_series,
            'product': product,
            'seriers_id':seriers_id,
            'product_id': product_id
        })
