from flask import Flask, url_for, render_template

# __name__ lets flask know the root path of the application
# to locate resources like templates
app = Flask(__name__)


# get_image function returns the url of an image file, in the static folder
def get_image(name_filetype):
    return url_for('static', filename=name_filetype)


# returns the home page template, title and image variables are accessed in index_pet.html
# render_template is a flask function that generates an output from a template file
@app.route('/')
def home():
    return render_template('index_pet.html', title='HOME | Pet Adoption Center', image=get_image)


# returns a template of a dog's profile, the pet's name is assigned to the name variable
@app.route('/dog/<name>')
def dog(name):
    return render_template(f'{name}.html', title=f'{name.upper()} | Pet Adoption Center', image=get_image,
                           name=name.capitalize())


# returns a template with a cat's profile, the pet's name is assigned to the name variable
@app.route('/cat/<name>')
def cat(name):
    return render_template(f'{name}.html', title=f'{name.upper()} | Pet Adoption Center', image=get_image,
                           name=name.capitalize())


# returns a template with a gallery of either cats or dogs, determined bby the animal variable
@app.route('/<animal>')
def all_animals(animal):
    return render_template(f'{animal}.html', title=f'{animal.upper()} | Pet Adoption Center', image=get_image,
                           animal=animal.capitalize())


if __name__ == '__main__':

    app.run(debug=True)

    # app.shutdown()
