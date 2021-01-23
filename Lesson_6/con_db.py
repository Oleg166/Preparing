from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PATH_DB = 'db.sqlite3'
Base = declarative_base()
ENGINE = create_engine(f'sqlite:///{PATH_DB}')


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(40), unique=True, nullable=False)
    category_description = Column(String(300), nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description
    
    def __repr__(self):
        return f"Категория {self.category_name}"


class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit = Column(String(20), unique=True, nullable=False)

    def __init__(self, unit):
        self.unit = unit
    
    def __repr__(self):
        return f"Единица измерения {self.unit}"


class Positions(Base):
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column(String(20), unique=True, nullable=False)

    def __init__(self, position):
        self.position = position
    
    def __repr__(self):
        return f"Должность {self.position}"


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(30), unique=True, nullable=False)
    good_unit = Column(Integer, ForeignKey('units.unit_id'))
    good_cat = Column(Integer, ForeignKey('categories.category_id'))

    def __init__(self, good_name):
        self.good_name = good_name
    
    def __repr__(self):
        return f"Товар {self.good_name}"


class Employees(Base):
    __tablename__ = 'employees'
    employe_id = Column(Integer, primary_key=True)
    employe_fio = Column(String(70), nullable=False)
    employe_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, employe_fio):
        self.employe_fio = employe_fio
    
    def __repr__(self):
        return f"Сотрудник {self.employe_fio}"


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50), unique=True, nullable=False)
    vendor_ownerchipform = Column(String(50), nullable=False)
    vendor_address = Column(String(200), nullable=False)
    vendor_phone = Column(String(20), unique=True, nullable=False)
    vendor_email = Column(String(20), nullable=False)

    def __init__(self, vendor_name, vendor_ownerchipform,
                 vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return f"Поставщик {self.vendor_name}"
    

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
SESS_OBJ = Session()
categ = Categories("Что-то", "очень нужное")
vend = Vendors('TSMC', 'open', 'Taiwan', '999999999', 'tsmc@taiwan.tw')
SESS_OBJ.add(categ)
SESS_OBJ.add(vend)
SESS_OBJ.commit()

print(categ)
print(vend)
