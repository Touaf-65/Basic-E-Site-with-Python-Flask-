from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models import User, db
#from . import auth

auth = Blueprint("auth", __name__)


@auth.route("/signUpPage", methods=["GET", "POST"])
def signUpPage():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if password != password2:
            flash("Mot de passe incompatibles")
            return redirect(url_for("auth.signUpPage"))
        
        elif len(str(password)) < 8:
            flash('Password should have at least 8 characters')
            return redirect(url_for('auth.signUpPage'))

        elif len(firstname) < 2 or len(lastname) < 2:
            flash('The first and last names must exceed 2 characters')
            return redirect(url_for('auth.signUpPage'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(name=str(firstname)+' '+str(lastname), email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash("Enregistrement réussi!", "success")
        return redirect(url_for("auth.loginPage"))

    return render_template("signUpPage.html")

#----LOGIN CONTROL----

@auth.route('/loginPage', methods=["GET", "POST"])
def loginPage():
     return render_template('loginPage.html')

@auth.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                return render_template('home.html')
            else:
                flash(" mot de passe incorrect", "danger")
                return render_template('loginPage.html')       
        else:
            flash("Adresse e-mail incorrect", "danger")
            return render_template('loginPage.html')  
              
    return render_template("loginPage.html")



#------------------BY TOUAFIC BOUAB---------------------------------------

# @auth.route("/signUpPage", methods=["GET", "POST"])
# def signUpPage():
#     if request.method == "POST":
#         firstname = request.form.get("firstname")
#         lastname = request.form.get("lastname")
#         email = request.form.get("email")
#         password = request.form.get("password")
#         password2 = request.form.get("password2")

#         if not lastname or not firstname or not email or not password or not password2:
#             flash("Veuillez remplir tous les champs", "danger")
#             return redirect(url_for("auth.signUpPage"))

#         existing_user = User.query.filter_by(email=email).first()
#         if existing_user:
#             flash("Cet utilisateur existe déjà", "danger")
#             return redirect(url_for("auth.signUpPage"))

#         if password != password2:
#             flash("Mot de passe incompatibles")
#             return redirect(url_for("auth.signUpPage"))

#         if len(str(password)) < 8:
#             flash('Password should have at least 8 characters')
#             return redirect(url_for('auth.signUpPage'))

#         if len(firstname) < 2 or len(lastname) < 2:
#             flash('The first and last names must exceed 2 characters')
#             return redirect(url_for('auth.signUpPage'))

#         hashed_password = generate_password_hash(password, method='sha256')
#         new_user = User(name=str(firstname)+' '+str(lastname), email=email, password=hashed_password)

#         db.session.add(new_user)
#         db.session.commit()

#         flash("Enregistrement réussi!", "success")
#         return redirect(url_for("auth.loginPage"))

#     return render_template("signUpPage.html")




# @auth.route("/loginPage", methods=["GET", "POST"])
# def loginPage():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if not email or not password:
#             flash("Veuillez remplir tous les champs", "danger")
#             return redirect(url_for("auth.loginPage"))

#         user = User.query.filter_by(email=email).first()
#         if not user:
#             flash("Cet utilisateur n'existe pas", "danger")
#             return redirect(url_for("auth.loginPage"))

#         if check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for("home"))

#         flash("Adresse e-mail ou mot de passe incorrect", "danger")
#         return redirect(url_for("auth.loginPage"))

#     return render_template("loginPage.html")

#----------------------END TOUAFIC CODE-------------------------------------


#----------------------HERE ARE VIEWS----------------------

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.loginPage"))


@auth.route('/forgotPassword')
def forgotPassword():
    return render_template('forgotPassword.html')



@auth.route('/about')
def about():
    return render_template('about.html')


@auth.route('/about2')
def about2():
    return render_template('about2.html')


@auth.route('/home2')
def home2():
    return render_template('home.html')


@auth.route('/categories')
def categories():
    return render_template('categories.html')