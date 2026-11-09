from fastapi import FastAPI
app = FastAPI(
title="FastAPI Template",
description="A simple fastAPI template",
version="1.0.0"
)
@app.get("/")
def read_root():
   return {"massage ": "welcome tho the fastAPI template!"}

@app.get("/health")
def read_health():
   return{"status": "ok"}