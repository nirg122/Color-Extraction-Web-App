import extcolors
import os
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images/upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def extract_colors(file):
    # Extracting Colors From Image
    colors, pixel_count = extcolors.extract_from_path(f"static/images/upload/{file}")

    # Making a list of only the rgb codes
    colors_list = []
    for i in range(len(colors)):
        lists = []
        for _ in range(3):
            lists.append(colors[i][0][_])
        colors_list.append(lists)
    # Converting the rgb code to hex coeds
    hex_color_list = []
    for index in range(len(colors_list)):
        r = colors_list[index][0]
        g = colors_list[index][1]
        b = colors_list[index][2]
        hex_color_list.append('#%02x%02x%02x' % (r,g,b))
    return hex_color_list


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'mkDiot68n5jksSDSAtkSDF13ntjk45nt'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/image_colors", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # deleting existing files from dir
        directory = 'static/images/upload'
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            hex_color_list = extract_colors(filename)
            return render_template("index.html", name=filename, colors=hex_color_list)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
