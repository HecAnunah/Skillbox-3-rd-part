from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField
from wtforms.validators import InputRequired, Email, Regexp, EqualTo

app = Flask(__name__)
# app.secret_key = 'secret'


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = StringField(
        validators=[
            InputRequired(),
            Regexp(r"^\d{10}$", message="Не верный формат ввода телефона"),
        ]
    )
    name = StringField(
        validators=[
            InputRequired(),
            Regexp(
                r"^[А-ЯЁ][а-яё]+ [А-ЯЁ].[А-ЯЁ]\.$",
                message="Не верный формат ввода имени",
            ),
        ]
    )
    address = StringField(validators=[InputRequired()])
    index = IntegerField()
    comment = StringField()


class LotaryForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    surename = StringField(validators=[InputRequired()])
    ticket = StringField(validators=[InputRequired(), Regexp(r"^[1-9]\d{5}$")])

# ИГРАЛ С Филдами
class ChangePassword(FlaskForm):
    password = PasswordField(
        "Enter new passowrd",
        validators=[InputRequired(), EqualTo("comfrim_password", message="Error")],
    )
    comfrim_password = PasswordField(
        "comfrim_password you password", validators=[InputRequired()]
    )


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


def _valid_ticket(tck):
    first_half = sum(int(num) for num in tck[:3])
    second_half = sum(int(num) for num in tck[3:])

    return first_half == second_half


@app.route("/lotary", methods=["POST"])
def lotary():
    form = LotaryForm()
    if form.validate_on_submit():
        name, surename, ticket = form.name.data, form.surename.data, form.ticket.data
        if _valid_ticket(ticket):
            return f"Поздравляем {name} {surename} вы победили в лотерею!"
        else:
            return f"Сожалеем {name} {surename} вы победите в другой раз!"

    return f"Ошибка: {form.errors}", 400


@app.route("/change_password", methods=["POST"])
def change_password():
    form = ChangePassword()
    if form.validate_on_submit():
        password = form.password.data
        return f"Вы сменили пароль на new_password = {password}"
    return f"ОШИБКА: {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
