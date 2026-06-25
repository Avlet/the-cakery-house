from pydantic import BaseModel
from typing import Optional

# बेस प्रोडक्ट स्कीमा
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: str
    category: str
    rating: float = 4.5
    delivery_time: str = "30-45 Min"
    is_offer: int = 0  # 1 = Slider, 0 = Normal

# डेटाबेस में नया प्रोडक्ट डालने के लिए
class ProductCreate(ProductBase):
    pass

# फ्रंटएंड को रिस्पांस भेजने के लिए
class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True