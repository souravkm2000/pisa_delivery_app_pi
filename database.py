from sqlalchemy import create_engine  
 
 
engine=create_engine('postgresql://postgres:souravkm8@localhost/pizza delevery '
                     echo=ture 
                     
)

Base=declarative_base()

session=sessionmaker()

   