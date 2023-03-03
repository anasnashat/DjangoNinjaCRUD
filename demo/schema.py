from ninja import Schema, ModelSchema
from .models import Product

class CategorySchema(Schema):
    name: str
    slug: str


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ['name',  'category',  'web_id']
