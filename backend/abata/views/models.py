from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, DateTime, Text, Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String)
    role = Column(String, default="user")  # or "admin"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    profile = relationship("Profile", uselist=False, back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image = Column(String)  # store file path
    display_name = Column(String)
    address = Column(String)
    birthdate = Column(String)
    gender = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    user = relationship("User", back_populates="profile")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    description = Column(Text)
    image_path = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    category = relationship("Category", back_populates="products")

class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class DeliveryMethod(Base):
    __tablename__ = 'delivery_methods'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class TransactionStatus(Base):
    __tablename__ = 'transaction_statuses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    payment_id = Column(Integer, ForeignKey('payment_methods.id'))
    delivery_id = Column(Integer, ForeignKey('delivery_methods.id'))
    status_id = Column(Integer, ForeignKey('transaction_statuses.id'))
    address = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    payment = relationship("PaymentMethod")
    delivery = relationship("DeliveryMethod")
    status = relationship("TransactionStatus")
    details = relationship("TransactionDetail", back_populates="transaction")

class TransactionDetail(Base):
    __tablename__ = 'transaction_details'
    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)
    price = Column(Float)
    transaction = relationship("Transaction", back_populates="details")
    product = relationship("Product")

class Promo(Base):
    __tablename__ = 'promos'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    discount_percentage = Column(Float)
    image_path = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
