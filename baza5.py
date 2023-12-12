from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship('Address', back_populates='person', order_by='Address.email',cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __repr__(self):
        return self.email

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

anakin = Person(name='Anakin', age=38)
obi = Person(name='Obi Wan', age=45)

obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waka@gmail.com')
]

obi2 = Person(name="obi", age=45)
session.add(anakin)
session.add(obi)
session.add(obi2)

session.commit()

all_ = session.query(Person).all()
print(all_)

an1 = session.query(Person).first()
print(an1)
print(an1.id, an1.name, an1.addresses)

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()
print(obi_list)
for o in obi_list:
    print("id=", o.id, "name:", o.name, "age:", o.age, "email:", o.addresses)
