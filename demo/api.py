from typing import List

from ninja import NinjaAPI
from .schema import CategorySchema, ProductSchema
from .models import Category, Product

api = NinjaAPI()

#  add category
@api.post('/add_category')
def add_category(request, data: CategorySchema):
    cate = Category.objects.create(**data.dict())
    return {'id': cate.id}

#  add product
@api.post('add-product')
def add_product(request, data: ProductSchema):
    pro = Product.objects.create(**data.dict())
    return {'id': pro.id}

# get all category
@api.get('category/all', response=List[CategorySchema])
def get_all_category(request):
    cate = Category.objects.all()
    return cate

#  get all product
@api.get('product/all', response=List[ProductSchema])
def get_all_products(request):
    pro = Product.objects.all()

    return pro

# get product by category
@api.get('product/all/category/{category_slug}', response=List[ProductSchema])
def get_product_by_category(request ,category_slug: str):
    pro = Product.objects.filter(category__slug=category_slug)
    return pro