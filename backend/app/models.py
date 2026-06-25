from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    address = Column(String, nullable=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    category = Column(String) # Cakes, Snacks, Desserts etc.
    rating = Column(Float, default=4.5)
    delivery_time = Column(String, default="30-45 Min")
    is_offer = Column(Integer, default=0) # 1 = Show in Hero Slider, 0 = Normal

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(Float, nullable=False)
    # Status: 'Placed', 'Baking', 'Out for Delivery', 'Delivered'
    status = Column(String, default="Placed") 
    created_at = Column(DateTime, default=datetime.utcnow)