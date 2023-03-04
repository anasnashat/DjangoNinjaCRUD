from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Form, File, UploadedFile
from .schema import CategorySchema, ProductSchema
from .models import Category, Product, Media

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
def get_product_by_category(request, category_slug: str):
    pro = Product.objects.filter(category__slug=category_slug)
    return pro


@api.put('edite/category/{category_id}')
def update_category(request, category_id: int, data: CategorySchema):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in data.dict().items():
        if value:
            setattr(category, attr, value)

    category.save()

    return {'success': True}


@api.patch('edite/product/{product_id}')
def update_product(request, product_id: int, data: ProductSchema):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in data.dict().items():
        if value:
            setattr(Product, attr, value)
    product.save()

    return {'success': True}


@api.delete('delete/category/{category_id}')
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()

    return {'result': f'deleted category name :  {category.name}.  success'}


@api.post("category/form")
def post_category_form(request, form: CategorySchema = Form(...)):
    category = Category.objects.create(**form.dict())
    return {'name': category.name}


@api.post("category/form/params")
def post_category_form_params(request, name: str = Form(...), slug: str = Form(...)):
    category = Category.objects.create(name=name, slug=slug)
    return {"name": category.name}


@api.post("upload/product/image")
def upload_media(request, prod_id: int = Form(...), file: UploadedFile = File(...)):
    product = get_object_or_404(Product, id=prod_id)
    media = Media.objects.create(img_url=file, product_inventory=product)
    return {"id": media.id}
