from sqlalchemy.orm import Session
from src.db.main import UserSessionLocal
from src.db.models import User

# Create a new session
db: Session = UserSessionLocal()

# Query all users
users = db.query(User).all()

print("ID | Username | Email")
for user in users:
    print(f"{user.id} | {user.username} | {user.email}")

db.close()
