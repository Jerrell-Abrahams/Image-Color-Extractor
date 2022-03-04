from PIL import Image
import extcolors
from flask import Flask, render_template, request, url_for
import os

UPLOAD_FOLDER = "C:/Users/Jerrell Abrahams/Desktop/Potfolio Projects/Image Colour Palette Generator/static"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def home():
    def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb


    if request.method == 'POST':
        if request.files['imgFile']:
            extracted_image = request.files["imgFile"]
            image_name = extracted_image.filename
            extracted_image.save(os.path.join(app.config["UPLOAD_FOLDER"], extracted_image.filename))
            img = Image.open(f"static/{image_name}")
            colors, pixel_count = extcolors.extract_from_image(img, tolerance=16, limit=10)

            list_colors = []
            for color in colors:
                list_colors.append((rgb_to_hex(colors[colors.index(color)][0]), int(colors[colors.index(color)][1] /pixel_count * 100)))


            return render_template("index.html", image=image_name, colors=list_colors)
        else:
            default_image = "5g9r54.jpg"
            return render_template("index.html", image=default_image)

    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

