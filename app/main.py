from fastapi import FastAPI


app = FastAPI()


@app.get("/json")
def get_json():
    # Возвращаем JSON-ответ
    return {
        "name": "fastapi",
        "description": "API for data",
        "port": "8000",
        "available": True
    }
