#!/usr/bin/python3
import sqlalchemy
#from  import Table, Column, Integer, String, MetaData
meta = MetaData()

Base = Table(
   'Base', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

State = Table(
   'states', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)
