from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
class Ticket(Base):
    __tablename__ = 'tickets' #Mapped[int] indicates that its Python type is an integer.mapped_column() defines its database configuration.
    id:Mapped[int] =mapped_column(Integer,primary_key=True)
    customer_name:Mapped[str]= mapped_column(String(100))
    customer_email:Mapped[str]= mapped_column(String(225))
    subject:Mapped[str]= mapped_column(String(250))
    description:Mapped[str]=mapped_column(Text)
    status:Mapped[str]=mapped_column(String(200),default='open')
    category:Mapped[str]= mapped_column(String(50),default="General Inquiry")
    sentiment:Mapped[str]= mapped_column(String(100),default="neutral")