from database import Base
from sqlalchemy import column,Integer,Boolean,text,String


class user(Base):
    tablename="user"
    id=column(Integer,primary_key=True)
    username=column(string(25),unique=True)
    email=column(string(80),unique=True)
    password=column(text,nullable=True)
    is_staff=column(Boolean,default=False)
    is_active=column(Boolean,default=False)
    
    
def _repr_(self): 
    returnf"<user{self.username}"
    
    
    
    
class choice(Base):
    ORDER_STATUSES=(
        ("PENDING","pending"),
        ("IN-TRANSIT","in-transit"),
        ("DELIVERED","deliverd")
        
    ) 
    
    PIZZA_SIZES=(
        ("SMALL","small"),
        ("MEDIUM","medium"),
        ("LARGE","large"),
        ("EXTRA-LARGE","extra-large")
        
    )   
    
    tablename="order"
    id=column(Integer,primary_key=True) 
    quantity=column(integer,nullable=False)
    order_status=column(choicetype(choices=ORDER_STATUSES),default="PENDING ")
    
    
    
      