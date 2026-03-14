from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(String(50), nullable=False)
    receiver_id = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(String(20), default='2026-03-14 12:38:01')  # Replace with a datetime field for actual use

    def __repr__(self):
        return f"<Message(id={self.id}, sender_id='{self.sender_id}', receiver_id='{self.receiver_id}', content='{self.content}', timestamp='{self.timestamp}')>",
