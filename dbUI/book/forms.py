from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Email, NumberRange

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field
class BookForm(FlaskForm):
    ISBN = IntegerField(
        label = "ISBN",
        validators = [NumberRange(message = "ISBN is a required field.")]
    )

    Title = StringField(label = "Title", validators = [DataRequired(message = "Title is a required field.")])

    Publisher = StringField(label = "Publisher", validators = [DataRequired(message = "Publisher is a required field.")])
    
    Page_number = IntegerField(
        label = "Number of pages",
        validators = [NumberRange(message = "Number of pages is a required field.")]
    )
    
    Summary = StringField(label = "Summary", validators = [DataRequired(message = "Summary is a required field.")])

    Available_copies = IntegerField(
        label = "Available copies",
        validators = [NumberRange(min = 0, message = "Available copies is a required field.")]
    )

    img = StringField(label = "Image", validators = [DataRequired(message = "Image is a required field.")])

    B_language = StringField(label = "Book's Language", validators = [DataRequired(message = "Language is a required field.")])

    Authors = StringField(label = "Authors", validators = [DataRequired(message = "Authors is a required field.")])

    Category = SelectMultipleField(label="Category",
        choices=[
            ("Biography", "Biography"),
            ("Cooking", "Cooking"),
            ("Fantasy", "Fantasy"),
            ("Fiction", "Fiction"),
            ("History", "History"),
            ("Mystery", "Mystery"),
            ("Romance", "Romance"),
            ("Science Fiction", "Science Fiction"),
            ("Self-Help", "Self-Help"),
            ("Thriller", "Thriller")],
        validators=[DataRequired(message="Category is a required field.")])

    Key_words = StringField(label = "Key words", validators = [DataRequired(message = "Key words is a required field.")])

    submit = SubmitField("Create")
