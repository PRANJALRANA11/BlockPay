from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import firestore, credentials

from server.request_and_response import NFTRequest

app = FastAPI()
cred = credentials.Certificate("server/cred/credentials.json")
default_app = firebase_admin.initialize_app(cred)


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
async def post_nft(user_request: NFTRequest):
    # this nft reuest stores in the database then if sucessfull then return 201 response code and we got the postive response

    return {"message": "NFT has been stored!"}




