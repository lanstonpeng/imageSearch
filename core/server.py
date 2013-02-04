import os
from flask import Flask,request,redirect,url_for
from werkzeug import secure_filename
from PIL import Image
from core import *

UPLOAD_FOLDER = "/upload"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def test(val="none"):
    return "testing"+val 

@app.route("/upload",methods=['GET','POST'])
def upload_file():
    print "test"
    if request.method =="POST":
        x = request.form.get("x",0,type=int)
        y = request.form.get("y",0,type=int)
        w = request.form.get("w",0,type=int)
        h = request.form.get("h",0,type=int)
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save("upload/"+filename)
        img = Image.open("upload/"+filename)
        box = (x , y , x+w, y+h)
        cropp = img.crop(box)
        cropp.save("cropped/"+filename)

        #start calculating
        engine = Engine()
        img = engine.loadImage("cropped/"+filename)
        imggrey = engine.greytifyImg(img)
        engine.extractSURF(imggrey)
        engine.trainKNN()
        result = engine.matching()
        print result

        #return redirect(url_for("/"))
    return "get nothing"


if __name__ == '__main__':
    app.run(debug=True,port=8888)
