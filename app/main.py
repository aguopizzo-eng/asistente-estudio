from fastapi import FastAPI

app = FastAPI(title="Asistente de Estudio")

@app.get("/")
def inicio():
    return {"mensaje": "Hola, asistente de estudio"}
