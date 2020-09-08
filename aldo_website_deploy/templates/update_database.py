from app_with_dutch_course import db
from app_with_dutch_course import Tests

db.create_all()
#change value of id to edit id'th row
update_data = Tests.query.filter_by(id=1).first()
update_data.question="Gezellig"

db.session.commit()