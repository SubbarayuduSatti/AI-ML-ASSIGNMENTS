from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_msg():
    return {
        "message": "Hello World"
    }

@app.get("/data")
def get_data():
    return {
        "name": "Subbarayudu Satti",
        "Address":"Hyderabad",
        "language": ["javascript", "c++", "python"]
    }