from app import db
from sqlalchemy.dialects.postgresql import JSONB


class IdMixin:
    id = db.Column(db.Integer, primary_key=True)


class TimeStampMixin:
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


class User(db.Model, IdMixin, TimeStampMixin):
    __tablename__ = 'user'

    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)


class Item(db.Model, IdMixin, TimeStampMixin):
    __tablename__ = 'item'

    name = db.Column(db.String(128), unique=True)
    brand = db.Column(db.String(64))
    category = db.Column(db.String(64))
    product_code = db.Column(db.String(128))
    variants = db.relationship('Variant', backref='item', lazy='dynamic')


class Variant(db.Model, IdMixin, TimeStampMixin):
    __tablename__ = 'variant'

    name = db.Column(db.String(128), unique=True)
    cost_price = db.Column(db.Integer)
    selling_price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    properties = db.Column(JSONB, default=lambda: {})
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))


class UserActivity(db.Model, IdMixin):
    """
    We're assuming that we will insert to this table everytime one of the following happens:
    1)  An Item's attribute is updated
    2)  A new Variant is added or existing Variant is deleted
    3)  A Variant's attribute is updated, could be adding/removing properties to JSONB column as well
    """
    __tablename__ = 'user_activity'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    user = db.relationship('User', lazy='joined')

    # variant or item whose attributes are being changed appended by it's ID e.g. variant 1 or item 5
    item_identifier = db.Column(db.String(32))

    # could be one of 'edited', 'added a variant', 'deleted a variant'
    change_type = db.Column(db.String(64))

    # name of the attribute being edited, for adding/deleting a variant, it would be "variants"
    attribute_name = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True)
