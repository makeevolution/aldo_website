from app_with_dutch_course import app

for i in app.url_map.iter_rules():
    print(i.endpoint)