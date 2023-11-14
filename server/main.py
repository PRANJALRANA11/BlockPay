from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# added CORS middleware to allow requests from the frontend
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home_screen_of_api():
    return {"message": "Welcome to the API of the BlockPay Project!"}


# Now, I have to build a way to store information to the database
@app.post("/nft")
async def post_nft():
    return {"message": "NFT has been stored!"}




