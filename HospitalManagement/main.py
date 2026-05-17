from fastapi import FastAPI
import uvicorn
from routes import hospital_router


app = FastAPI(
    # docs_url=None,
    # redoc_url="/redoc",
)

app = FastAPI(title="Hospital Directory API")

app.include_router(hospital_router)


@app.get("/")
def health_check():
    return {"status": "running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",   # 👈 IMPORTANT (module path, not file path)
        host="0.0.0.0",
        port=8000,
        reload=True
    )
