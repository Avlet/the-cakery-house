from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)

# 1. सारे प्रोडक्ट्स फ़ेच करने की API (Filter by category optional)
@router.get("/", response_model=List[schemas.ProductResponse])
def get_products(category: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category.getattr(category))
    return query.all()

# 2. सिर्फ ऑफर्स (Slider items) फ़ेच करने की API
@router.get("/offers", response_model=List[schemas.ProductResponse])
def get_offers(db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.is_offer == 1).all()

# 3. डमी डेटाबेस लोड करने के लिए एक हेल्पर रूट
@router.post("/setup-dummy", status_code=201)
def setup_dummy_data(db: Session = Depends(get_db)):
    # चेक करें कि डेटा पहले से तो नहीं है
    if db.query(models.Product).count() > 0:
        return {"message": "Dummy data already exists!"}
        
    dummy_cakes = [
        # Slider Offers
        models.Product(name="Natural & Healthy Cake", description="Organic sweetness baked with love.", price=549.0, image_url="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=500", category="Cakes", is_offer=1),
        models.Product(name="Fresh Chocolate Truffle", description="Indulge in premium rich Belgian chocolate.", price=649.0, image_url="https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=500", category="Cakes", is_offer=1),
        
        # Regular Bakery Items (Popular Picks & Best Sellers)
        models.Product(name="Chocolate Mud", description="Rich muddy delight", price=549.0, image_url="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=500", category="Cakes", is_offer=0),
        models.Product(name="Chocolate Kitkat", description="Crunchy Kitkat cake", price=549.0, image_url="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=500", category="Cakes", is_offer=0),
        models.Product(name="Chocolate Truffle", description="Classic Truffle", price=549.0, image_url="https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=500", category="Cakes", is_offer=0),
        models.Product(name="Keva Special", description="Chef special blend", price=549.0, image_url="https://images.unsplash.com/photo-1519869325930-281384150729?w=500", category="Snacks", is_offer=0),
        models.Product(name="Premium Walnut", description="Loaded with walnuts", price=549.0, image_url="https://images.unsplash.com/photo-1603532648955-039310d9ed75?w=500", category="Chocolates", is_offer=0),
    ]
    
    db.add_all(dummy_cakes)
    db.commit()
    return {"message": "Dummy products inserted successfully!"}