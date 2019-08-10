from flask import Blueprint, request, jsonify
from flask_rest_api.models import Product, ProductSchema
from flask_rest_api.extensions import db

main = Blueprint("main", __name__)


@main.route("/product", methods=["POST"])
def add_product():
    product_schema = ProductSchema(strict=True)

    new_product = Product(
        name=request.json["name"],
        description=request.json["description"],
        price=request.json["price"],
        qty=request.json["qty"],
    )

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


@main.route("/product", methods=["GET"])
def get_products():
    products_schema = ProductSchema(many=True, strict=True)
    all_products = Product.query.all()
    result = products_schema.dump(all_products).data
    return jsonify(result)


@main.route("/product/<int:id>", methods=["GET"])
def get_single_product(id):
    product_schema = ProductSchema(strict=True)
    product = Product.query.get(id)
    # result = product_schema.jsonify(product)
    # or
    result = product_schema.dump(product).data
    return jsonify(result)
    # return result


@main.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
    product_schema = ProductSchema(strict=True)
    product = Product.query.get(id)

    product.name = request.json["name"]
    product.description = request.json["description"]
    product.price = request.json["price"]
    product.qty = request.json["qty"]

    db.session.commit()

    return product_schema.jsonify(product)


@main.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    product_schema = ProductSchema(strict=True)
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)
