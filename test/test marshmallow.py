from pprint import pprint
from marshmallow import Schema, fields
import datetime as dt


class Tank:
    def __init__(self, model: str, weight: int, cruew: int) -> None:
        self.model = model
        self.weight = weight
        self.cruew = cruew

    def repair(self, weight_detail):
        self.weight += weight_detail


class TankSchema(Schema):
    model = fields.String()
    weight = fields.Int()
    cruew = fields.Int()


class Army:
    def __init__(self, units: list, name: str) -> None:
        self.name = name
        self.units = units.copy()


class ArmySchema(Schema):
    name = fields.Str()
    # units = fields.List(fields.Nested(TankSchema(only=("model",))))
    units = fields.Nested(TankSchema, many=True)


tank1 = Tank('T90', 150, 3)
tank2 = Tank('T90-2', 250, 3)
tank3 = Tank('T90-3', 950, 2)
tank4 = Tank('T90-4', 194, 5)
army = Army([tank1, tank2, tank3, tank4], '1-st army')
# print(army.name, army.units)

sc = ArmySchema()
r = sc.dump(army)
print(r)

#
#  class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.created_at = dt.datetime.now()
#         self.friends = []
#         self.employer = None


# class Blog:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author  # A User object


# class UserSchema(Schema):
#     name = fields.String()
#     email = fields.Email()
#     # Use the 'exclude' argument to avoid infinite recursion
#     employer = fields.Nested(lambda: UserSchema(exclude=("employer",)))
#     friends = fields.List(fields.Nested(lambda: UserSchema()))

#     # class Meta:
#     #     ordered = True


# class BlogSchema(Schema):
#     title = fields.String()
#     author = fields.Nested(UserSchema)


# user = User("Steve", "steve@example.com")
# user.friends.append(User("Mike", "mike@example.com"))
# user.friends.append(User("Joe", "joe@example.com"))
# user.employer = User("Dirk", "dirk@example.com")
# result = UserSchema().dump(user)
# pprint(result, indent=2)
