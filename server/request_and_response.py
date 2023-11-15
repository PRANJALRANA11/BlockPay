from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class NFTRequest(BaseModel):
    name: str
    ammount: float
    description: str | None = None
    sender: str
    address: str
    nft: str
    
class NFTResonse(BaseModel):
    user_id: int
    nft_id: int
    name: str
    description: str | None = None

# sender, address, sender amount , sender, description , creator address , creator, nft