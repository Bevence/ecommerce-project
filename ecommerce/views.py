from django.db import models
from django.db.models.fields import IPAddressField
from ecommerce.context_processors import categories, subcategories
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from ecommerce.models import Category, Items, Subcategory
# from django.views.decorators.cache import cache_page

# Create your views here.
# @cache_page(10*60)
class EcommerceTemplateView(TemplateView):
    template_name = 'index.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = {}
        category = Category.objects.filter(trending = True)[0]
        subcategories = Subcategory.objects.filter(category=category)[:6]
        for sub in subcategories:
            items[sub.title] = Items.objects.filter(category=sub)
        new_arrivals = Items.objects.order_by('-created_date')[:4]
        featured_items = Items.objects.filter(featured = True)
        trend_items = Items.objects.filter(category__in=subcategories)
        deals = Items.objects.filter(deal_of_day=True).order_by('-created_date')[:2]
        context['subcategories'] = subcategories
        context['new_arrivals'] = new_arrivals
        context['featured_items'] = featured_items
        context['trend_items'] = trend_items
        context['deals'] = deals
        return context



class ItemsListView(ListView):
    model = Items
    # queryset = Items.objects.order_by('-created_date')
    paginate_by = 6
    template_name = "product/items.html"

    def get_queryset(self):
        items = self.model.objects.order_by('created_date')
        return items
    
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        sub_categories_list = {}
        for category in categories:
            sub_categories_list[category.title] = Subcategory.objects.filter(category=category)
        context['items_count'] = Items.objects.all().count()
        context['categories'] = categories
        context['sub_categories_list'] = sub_categories_list
        return context
    
 
class SubCategoryListView(ListView):
    model = Items
    paginate_by = 6
    template_name = "product/category_item.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = Subcategory.objects.filter(slug=self.kwargs['sub_category'])
        items = Items.objects.filter(category__in=subcategory)
        # print(items)
        context["items"] = items
        return context
    
 

class CategoryListView(ListView):
    model = Items
    template_name = "product/category_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['category'])
        sub_categories = Subcategory.objects.filter(category__in=category)
        items = Items.objects.filter(category__in=sub_categories)
        context["items"] = items 
        return context
    




class CategoryItemView(View):
    def get(self, request, category):
        return render(request, 'product/sub_category_item.html')


class ItemDetailView(DetailView):
    model = Items
    template_name = 'product/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        return context
        

