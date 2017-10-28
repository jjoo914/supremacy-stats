from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from .base import Base


class Game(Base):
    # Table name
    __tablename__ = 'sp_games'

    #
    # Columns
    # -------------

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    game_host = Column(String)
    start_at = Column(DateTime)
    end_at = Column(DateTime)

    #
    # Relationships
    # -------------

    map_id = Column(Integer, ForeignKey('sp_maps.id'))
    map = relationship("Map", back_populates="games")

    players = relationship("Player", back_populates="game", lazy="dynamic")

    days = relationship("Day", back_populates="game")

    relations = relationship("Relation", back_populates="game", lazy="dynamic")

    coalitions = relationship("Coalition", back_populates="game")

    #
    # Attributes
    # -------------

    @hybrid_method
    def day(self):
        delta = datetime.today() - self.start_at
        return delta.days

    #
    # Representation
    # -------------

    def __repr__(self):
        return "<Game(%s)>" % (self.id)
