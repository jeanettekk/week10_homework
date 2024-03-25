from flask import Flask, url_for, render_template

# __name__ lets flask know the root path of the application
# to locate resources like templates
app = Flask(__name__)


def get_image(name_filetype):

    return url_for('static', filename=name_filetype)


@app.route('/')
def home():
    return render_template('index_pet.html', title='HOME | Pet Adoption Center', image=get_image)


@app.route('/dog/<name>')
def dog(name):

    return render_template(f'{name}.html', title=f'{name.upper()} | Pet Adoption Center', image=get_image,
                           name=name.capitalize())


@app.route('/cat/<name>')
def cat(name):
    return render_template(f'{name}.html', title=f'{name.upper()} | Pet Adoption Center', image=get_image,
                           name=name.capitalize())

# @app.route('/<animal>')
# def all_animals(animal)
#
#
#     return render_template()


if __name__ == '__main__':

    app.run(debug=True)

    # app.shutdown()