from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class NFTRequest(BaseModel):
    name: str
    ammount: int
    description: str | None = None
    


class NFTResonse(BaseModel):
    user_id: int
    nft_id: int
    name: str
    description: str | None = None
