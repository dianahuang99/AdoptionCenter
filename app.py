from flask import Flask, render_template, redirect, flash, session
from pkg_resources import register_namespace_handler
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_new_pet_form():
    """Show new pet form"""
    form = AddPetForm()
    if form.validate_on_submit():
        #get all the form info and make a new pet instance
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add_pet_form.html', form=form)

@app.route("/<int:pet_id>")
def show_pet_info(pet_id):
    """Show pet info"""
    pet = Pet.query.get(pet_id)
    return render_template("pet_info.html", pet=pet)

@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form)


@app.route("/<int:pet_id>/delete", methods=["POST"])
def delete_pet(pet_id):
    """Delete pet"""
    pet = Pet.query.get(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect("/")