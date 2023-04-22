from apiflask import Schema, fields
from apiflask.validators import Range


class BaseResponse(Schema):
    data = fields.Field()  # the data key
    code = fields.Integer()


class GoodsOut(Schema):  # list of short goods for response
    id = fields.Integer(metadata={'example': 2})
    name = fields.String(metadata={'example': 'Coffee'})

class GoodsOutCached(GoodsOut):
    price = fields.Float(metadata={'example': 55.99})


class GoodIn(Schema):  # one good with full fields
    name = fields.String(required=True, metadata={'example': 'Coffee'})
    price = fields.Integer(metadata={'example': 21})
    manufacture_date = fields.Date(metadata={'example': '2019-02-05'})
    picture_url = fields.String(metadata={'example': 'pic.com/mypic.jpg'})


class GoodOut(GoodIn):  # one good with full fields
    id = fields.Integer()


class OrdersOut(Schema):    # list of orders for responce
    id = fields.Integer(required=True)
    order_date = fields.Date()
    customer_name = fields.String()
    customer_email = fields.String()
    delivery_address = fields.String()
    status = fields.String()
    notes = fields.String()

    class Meta:
        ordered = True


class OrderGood(Schema):
    good_id = fields.Integer(required=True, validate=Range(
        min=1), metadata={'example': 1})
    ammount = fields.Integer(required=True, validate=Range(
        1, 1000), metadata={'example': 2})


class OrderIn(Schema):
    order_date = fields.Date(required=True, metadata={'example': '2022-11-05'})
    customer_name = fields.String(
        required=True, metadata={'example': 'Carlson'})
    customer_email = fields.String(metadata={'example': 'carlson@gmail.com'})
    delivery_address = fields.String(metadata={'example': 'Apatity'})
    notes = fields.String(metadata={'example': 'poor customer'})
    good_item = fields.List(fields.Nested(OrderGood()), required=True)


class MessageOk(Schema):
    id = fields.Integer()

class LoginIn(Schema):  # one good with full fields
    username = fields.String(required=True, metadata={'example': 'vic'})
    password = fields.String(metadata={'example': "mypass"})
