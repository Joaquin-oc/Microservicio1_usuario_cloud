from fastapi import FastAPI
from database import engine, Base
from routes import router
import time

# espera a que PostgreSQL esté listo
def create_tables():
    for i in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            print("Tablas creadas", flush=True)
            return
        except Exception as e:
            time.sleep(3)

create_tables()

app = FastAPI(title="MS1 - Usuarios")
app.include_router(router)