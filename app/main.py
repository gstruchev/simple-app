from fastapi import FastAPI

app = FastAPI(title="DevOps Portfolio App")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/")
def root():
    return {
        "message": "Hello from simple app!",
        "endpoints": ["/", "/health", "/version"],
    }