from pydantic import BaseModel, EmailStr, ConfigDict
from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
class CreateTicket(BaseModel):
    customer_name: str
    email: EmailStr
    subject: str
    description: str
    status: TicketStatus = TicketStatus.OPEN


class TicketStatusUpdate(BaseModel):

    status:TicketStatus

class TicketResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str
    status: TicketStatus
    category: str
    sentiment:str

    model_config = ConfigDict(from_attributes=True)
