from .models import User

users = {
    i: User(uid=i, name=f"User {i}", email=f"user{i}@localhost")
    for i in range(10)
}
