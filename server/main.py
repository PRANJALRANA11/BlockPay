from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage



from request_and_response import NFTRequest

app = FastAPI()
cred = credentials.Certificate("/home/deepesh/development/hack/pranjal/BlockPay/server/credential.json")
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://blockpay-74c84.appspot.com',

})


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



# First stroing the image and getting the image
@app.post("/image")
async def post_image(file: UploadFile = File(...)):
    try:
        bucket = firebase_storage.bucket("test")
        block = bucket.blob("test")
        block.upload_from_file(file, content_type="image/png")
        return {"message": "Image has been uploaded!"}
    except Exception as e:
        return {"message": f"Error in uploading the image: {str(e)}"}
    
    # block.upload_from_file(file, content_type="image/png")





# Now, I have to build a way to store information to the database
@app.post("/nft")
async def post_nft(user_request: NFTRequest):
    # this nft reuest stores in the database then if sucessfull then return 201 response code and we got the postive response

    return {"message": "NFT has been stored!"}




