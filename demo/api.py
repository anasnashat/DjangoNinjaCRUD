from ninja import NinjaAPI
from .schema import CategorySchema, ProductSchema
from .models import Category, Product

api = NinjaAPI()


@api.post('/add_category')
def add_category(request, data: CategorySchema):
    cate = Category.objects.create(**data.dict())
    return {'id': cate.id}


@api.post('add-product')
def add_product(request, data: ProductSchema ):
    pro = Product.objects.create(**data.dict())
    return {'id': pro.id}
