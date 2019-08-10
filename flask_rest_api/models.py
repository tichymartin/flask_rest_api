from flask_rest_api.extensions import db, ma
from marshmallow import post_load


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __repr__(self):
        return print(f"Product => {self.id}, {self.name},{self.description}, {self.price}, {self.qty}")


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product

# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(many=True, strict=True)
