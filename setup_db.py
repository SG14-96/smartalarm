from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud.user as crud
# Create tables
Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()

    # Create roles if they don't exist
    if not crud.get_role_by_name(db, "user"):
        crud.create_role(db, "user", "Regular user")

    if not crud.get_role_by_name(db, "admin"):
        crud.create_role(db, "admin", "Administrator")

    db.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
