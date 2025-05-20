from sqlalchemy import Table,Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

workout_routune_association_table = Table(
    'workout_routine_association',
    Base.metadata,
    Column('workout_id', Integer, ForeignKey('workouts.id')),
    Column('routine_id', Integer, ForeignKey('routines.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    workouts = relationship('Workout', back_populates='owner')
    routines = relationship('Routine', back_populates='owner')
 

class Workout(Base):
    "__tablename__" = 'workouts'
    id = Column(Integer,primary_key =True , index = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    routines= relationship('Routine', secondary=workout_routune_association_table, back_populates='workouts')


class Routine(Base):
    "__tablename__" = 'routines'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(DateTime, default=datetime.())
    workouts = relationship('Workout', secondary=workout_routune_association_table, back_populates='routines')

Workout.routines = relationship('Routine', secondary=workout_routune_association_table, back_populates='workouts')