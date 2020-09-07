from app import db
from app import Tests

data = Tests.query.all()
print(data)