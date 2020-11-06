#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)

    def __repr__(self):
        return "<User(name='%s', job_title='%s')>" % (
            self.name, self.job_title)

class CommunicateInformation(Base):
    __tablename__ = 'communicate_info'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="communicate_information")

    def __repr__(self):
        return "<User(email='%s', mobile='%s')>" % (
            self.email, self.mobile)

User.communicate_information = relationship(
    "CommunicateInformation", order_by=CommunicateInformation.id, back_populates="user")
