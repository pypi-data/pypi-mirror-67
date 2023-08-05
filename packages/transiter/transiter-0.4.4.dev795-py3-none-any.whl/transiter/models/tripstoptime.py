from sqlalchemy import (
    Column,
    TIMESTAMP,
    DateTime,
    Index,
    Integer,
    String,
    Boolean,
    UniqueConstraint,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base, ToDictMixin


class TripStopTime(ToDictMixin, Base):
    __tablename__ = "trip_stop_time"

    pk = Column(Integer, primary_key=True)
    stop_pk = Column(Integer, ForeignKey("stop.pk"), nullable=False)
    trip_pk = Column(Integer, ForeignKey("trip.pk"), nullable=False)

    future = Column(Boolean, default=True, nullable=False)
    arrival_time = Column(TIMESTAMP(timezone=True))
    arrival_delay = Column(Integer)
    arrival_uncertainty = Column(Integer)
    departure_time = Column(DateTime(timezone=True))
    departure_delay = Column(Integer)
    departure_uncertainty = Column(Integer)
    stop_sequence = Column(Integer, nullable=False)
    track = Column(String)

    stop_id = None

    stop = relationship("Stop", back_populates="trip_times", cascade="none")
    trip = relationship(
        "Trip", back_populates="stop_times", cascade="none", cascade_backrefs=False
    )

    __table_args__ = (
        UniqueConstraint(trip_pk, stop_sequence),
        Index("trip_stop_time_stop_pk_arrival_time_idx", stop_pk, arrival_time),
    )

    _short_repr_list = [arrival_time, departure_time, track, future, stop_sequence]

    def to_dict(self):
        return {
            "arrival": {
                "time": self.arrival_time,
                "delay": self.arrival_delay,
                "uncertainty": self.arrival_uncertainty,
            },
            "departure": {
                "time": self.departure_time,
                "delay": self.departure_delay,
                "uncertainty": self.departure_uncertainty,
            },
            "track": self.track,
            "future": self.future,
            "stop_sequence": self.stop_sequence,
        }

    def get_time(self):
        return self.arrival_time or self.departure_time
