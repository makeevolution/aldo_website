from app import db
from app import Tests

db.create_all()

test_1=Tests(question='new1',answer='ansnew1')

db.session.add(test_1)
db.session.commit()