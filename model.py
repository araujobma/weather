from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()
metadata = Base.metadata

engine = create_engine("postgresql+psycopg2://user:mypass@postgres:5432/postgres")


class WeatherTask(Base):
    __tablename__ = "weather_task"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    task_group_id = Column(String, nullable=False)

    def __repr__(self):
        return f"WeatherTask(id={self.id}, created_at={self.created_at}, task_group_id={self.task_group_id})"

    def save(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    def get_by_id(id):
        with Session(engine) as session:
            return session.query(WeatherTask).filter_by(id=str(id)).first()
