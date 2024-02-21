import time
from fastapi import FastAPI


app = FastAPI()


@app.get("/wait")
def wait():
    time.sleep(0.5)
    return "done!"
