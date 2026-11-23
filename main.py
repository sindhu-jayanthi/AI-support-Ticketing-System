import asyncio

from fastapi import FastAPI, HTTPException,Depends,Query
from sqlalchemy import select
from gemini_services import classify_ticket,analyze_sentiment
from models import CreateTicket, TicketStatusUpdate,TicketResponse,TicketStatus
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from database_models import Ticket
from contextlib import asynccontextmanager


from database import create_tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
app = FastAPI(title="AI Ticket Support System",lifespan=lifespan)
@app.get("/")
async def home():
    return {"message":"AI Ticket Support System is running successfully"}


@app.post("/create-ticket",response_model=TicketResponse)
async def create_ticket(
    data: CreateTicket,
    db: AsyncSession = Depends(get_db)
):
    category, sentiment = await asyncio.gather(
        classify_ticket(data.description),
        analyze_sentiment(data.description)
    )
    new_ticket = Ticket(
        customer_name=data.customer_name,
        customer_email=data.email,
        subject=data.subject,
        description=data.description,
        status=data.status,
        category=category,
        sentiment=sentiment
    )

    db.add(new_ticket)

    await db.commit()

    await db.refresh(new_ticket)

    return new_ticket

@app.get("/tickets",response_model=list[TicketResponse])
async def get_tickets(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
        db:AsyncSession = Depends(get_db)):

    query= select(Ticket).order_by(Ticket.id.desc()).offset(skip).limit(limit)
    result= await db.execute(query)
    tickets=result.scalars().all()
    return tickets
@app.get("/tickets/filter", response_model=list[TicketResponse])
async def filter_tickets(status:TicketStatus,db:AsyncSession = Depends(get_db)):

    query= select(Ticket).where(Ticket.status==status)
    result= await db.execute(query)
    tickets=result.scalars().all()
    return tickets
@app.get("/tickets/{id}",response_model=TicketResponse)
async def get_ticket_byid(id:int,db:AsyncSession = Depends(get_db)):
     query= select(Ticket).where(Ticket.id==id)
     result= await db.execute(query)
     ticket=result.scalars().one_or_none()
     if not ticket:
         raise HTTPException(status_code=404, detail="Ticket not found")
     return ticket


@app.put("/ticket/{id}/status",response_model=TicketResponse)
async def update_status(id:int, data : TicketStatusUpdate, db:AsyncSession = Depends(get_db)):
    query= select(Ticket).where(Ticket.id==id)
    result=await db.execute(query)
    ticket=result.scalars().one_or_none()
    if not ticket:
        raise HTTPException(
                  status_code=404,
                  detail="Ticket not found"
        )
    ticket.status=data.status
    await db.commit()
    await db.refresh(ticket)
    return ticket

@app.delete("/tickets/{id}")
async def delete_ticket(id:int,db:AsyncSession=Depends(get_db)):
    query= select(Ticket).where(Ticket.id==id)
    result=await db.execute(query)
    ticket=result.scalars().one_or_none()
    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    await db.delete(ticket)
    await db.commit()
    return {"message":"Ticket deleted successfully"}

