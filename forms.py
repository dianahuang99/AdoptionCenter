from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, AnyOf, URL, NumberRange, Required

class AddPetForm(FlaskForm):
    name = StringField("Pet name", validators=[
                       InputRequired(message="Pet name cannot be blank")])
    species = StringField("Species", validators=[
                       InputRequired(message="Name cannot be blank"), AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField('Photo URL', validators=[URL(require_tld=True), Optional()])
    age = IntegerField('Age', validators=[
                       Optional(), NumberRange(min=0, max=30)])
    
    notes = StringField("Notes", validators=[
                       Optional()])
    
class EditPetForm(FlaskForm):
    
    photo_url = StringField('Photo URL', validators=[URL(require_tld=True), Optional()])
    
    
    notes = StringField("Notes", validators=[
                       Optional()])
    available = BooleanField('Available?')
    