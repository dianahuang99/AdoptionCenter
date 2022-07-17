"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
snowball = Pet(name="Snowball", species="Pomeranian", age=3, notes="She's the cutest.", photo_url='https://media.glamour.com/photos/56957ef55fff94d44eec2b1b/master/pass/entertainment-2014-08-biscuit-kat-main.jpg'
)

mochi = Pet(name="Mochi", species="Poodle", age=6, notes="She's soft!",photo_url='https://www.rd.com/wp-content/uploads/2019/01/shutterstock_673465372.jpg?fit=700,467')

flower = Pet(
    name="Flower", species="Bulldog", age=2, notes="Looks tough but is a sweetheart.",photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU8TzXwPCqtc3dOMNwQcoy1MNWvLUU_Bayrw&usqp=CAU'
)


# Add new objects to session, so they'll persist
db.session.add(snowball)
db.session.add(mochi)
db.session.add(flower)

# Commit--otherwise, this never gets saved!
db.session.commit()





