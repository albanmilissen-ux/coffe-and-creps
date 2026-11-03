from fastapi import FastAPI

app = FastAPI(title="Coffe and Creps API")


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "La API de Coffe and Creps esta funcionando."}
