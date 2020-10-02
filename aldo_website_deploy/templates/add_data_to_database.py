from app_with_dutch_course import db
from app_with_dutch_course import reflexief

db.create_all()

#change question and answer field to reflect what you want
test_1=reflexief(question='new1',answer='ansnew1')

db.session.add(test_1)
db.session.commit()