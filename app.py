from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://i.pinimg.com/564x/4b/6f/ec/4b6fec352ad65acf6c1265201432dfa1.jpg",
    "https://p1.pxfuel.com/preview/667/127/593/cat-baby-kitten-cat-domestic-cat-baby-cat-pet-royalty-free-thumbnail.jpg",
    "https://www.stockvault.net/data/2007/03/01/100489/thumb16.jpg",
    "https://thumbs.dreamstime.com/b/four-cute-cats-20687192.jpg",
    "https://thumbs.dreamstime.com/b/cute-cat-looking-up-to-sky-cut-cat-looking-up-to-sky-probably-some-birds-blurred-background-161011306.jpg",
    "https://cdn.pixabay.com/photo/2017/03/01/13/58/cat-2108536_960_720.jpg",
    "https://thumbs.dreamstime.com/b/four-cute-cats-20650677.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route('/special')
def special():
    url = "https://thumbs.dreamstime.com/b/four-cute-cats-20650677.jpg"
    return render_template('special.html', url=url)

if __name__ == "__main__":
        app.run(host="0.0.0.0")
