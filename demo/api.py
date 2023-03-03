from ninja import NinjaAPI
from .schema import CategorySchema
from .models import Category

api = NinjaAPI()


@api.post('/add_category')
def add_category(request, data: CategorySchema):
    cate = Category.objects.create(**data.dict())
    return {'id': cate.id}
