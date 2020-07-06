from manage import db, User
import os

# os.remove('tmp/manage.db')
# db.create_all()

# admin = User(user='tfjkv', income=0, food_ex=0,daily_ex=0,hobby_ex=0,last_ex=0,rent_cost=0,scholar=0,utility_cost=0,other=0)
# db.session.add(admin)
# db.session.commit()

data = User.query.filter_by(user='tfjkv').first()
print(data.income)