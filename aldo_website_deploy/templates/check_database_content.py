from app_with_dutch_course import db
from app_with_dutch_course import Tests

#just run this
data = Tests.query.all()
print(data)