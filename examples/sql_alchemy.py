import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define how to connect to the database
engine = create_engine(

    # TODO: change this to point to your MySQL instance!
    'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='mysecretpassword',url='localhost',db='postgres'), 
    
    # logging of SQL query
    echo=False
)

# Extend your objects from this class
Base = declarative_base()

# Define your objects and tables
class Fish(Base):
    __tablename__ = 'fishies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)

    def __str__(self):
        return f'{self.id} | {self.name} | {self.age}'

# create all the fishies
Base.metadata.create_all(engine)

# Create a database session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Insert fishies into our database
session.add_all([
    Fish(name='Bob', age=30),
    Fish(name='Allan', age=9),
    Fish(name='Joe', age=7),
    Fish(name='Simon', age=12),
    Fish(name='Michael', age=15)
])
session.commit()

# query fishes
print("All fishies:")
for f in session.query(Fish):
    print(f)


# query fishies with a filter
print("Fishies older than 10")
for f in session.query(Fish).filter(Fish.age > 10):
    print(f)

# get a fish by a specific id
print("Fishy with id 1")
f = session.query(Fish).filter(Fish.id == 1).one()
print(f)