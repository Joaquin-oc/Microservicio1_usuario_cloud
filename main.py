from fastapi import FastAPI
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import time

#correr tdo
#docker-compose up -d

#pararlo
#docker-compose down
#pararlo y borrar base d datos
#docker-compose down -v

#swagger: http://localhost:8000/docs
def create_tables():
    for i in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            print("Tablas creadas", flush=True)
            return
        except Exception as e:
            print(f"Esperando a PostgreSQL... intento {i+1}", flush=True)
            time.sleep(3)

create_tables()

app = FastAPI(title="MS1 - Usuarios")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)