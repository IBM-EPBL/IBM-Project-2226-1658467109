import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import requests
from flask import Flask, request, render_template, redirect, url_for
from cloudant.client import Cloudant
model = load_model(r"Updated-xception-diabetic-retinopathy.h5")
app = Flask(__name__)
# Authenticate using an IAM API key
client = Cloudant . iam('d3ffc21a-c9d1-4276-a7c3-d7a48a949e1f-bluemix',
                        'oS6rF9Lb8-d8IyJW4VEdHx5kiIN9ehQnNoj8ygKXFjzu', connect=True)
# Create a database using an initialized client
my_database = client.create_database('my_database')

# default home page or route
@app.route('/')
def index():
    return render_template('index.html')

@ app.route('/index')
def home():
    return render_template("index.html")

# registration page
@ app.route('/register')
def register():
    return render_template('register.html')

@ app.route('/afterreg', methods=['POST'])
def afterreg():
    x = [x for x in request.form.values()]
    print(x)
    data = {
        '_id': x[1],  # Setting id is optional
        'name': x[0],
        'psw': x[2]
    }
    print(data)
    query = {'_id': {'$eq': data['_id']}}
    docs = my_database.get_query_result(query)
    print(docs)
    print(len(docs.all()))
    if (len(docs.all()) == 0):
        url = my_database.create_document(data)
        return render_template("register.html", pred=" Registration Successful , please login using your details ")
    else:
        return render_template('register.html', pred=" You are already a nomber , please login using your details ")

# login page
@ app.route('/login')
def login():
    return render_template('login.html')

@ app.route('/afterlogin', methods=[' POST '])
def afterlogin():
    user = request.form['_id']
    passw = request.form['psw']
    print(user, passw)
    query = {'_id': {'$eq': user}}
    docs = my_database.get_query_result(query)
    print(docs)
    print(len(docs.all()))
    if (len(docs.all()) == 0):
        return render_template('login.html', pred="The username is not found.")
    else:
        if ((user == docs[0][0]['_ id'] and passw == docs[0][0]['psw'])):
            return redirect(url_for('prediction'))
        else:
            print('Invalid User')

@ app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route("/predict")
def predict():
    return render_template("prediction.html")

@ app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        f = request.files['image']
        # getting the current path 1.e where app.py is present
        basepath = os.path.dirname(__file__)
        #print ( " current path " , basepath )
        # from anywhere in the system we can give image but we want that
        filepath = os.path.join(basepath, 'uploads', f.filename)
        #print ( " upload folder is " , filepath )
        f.save(filepath)
        img = image.load_img(filepath, target_size=(299, 299))
        x = image.img_to_array(img)  # ing to array
        x = np.expand_dims(x, axis=0)  # used for adding one more dimension
        #print ( x )
        img_data = preprocess_input(x)
        prediction = np.argmax(model.predict(img_data), axis=1)
        # prediction = model.predict ( x ) #instead of predict_classes ( x ) we can use predict ( X ) ---- > predict_classes ( x ) gave error
        # print ( " prediction is prediction )
        index = [' No Diabetic Retinopathy ', ' Mild DR ',
                 ' Moderate DR ', ' Severe DR ', ' Proliferative DR ']
        # result = str ( index [ output [ 011 )
        result = str(index[prediction[0]])
        print(result)
        return render_template('prediction.html', prediction=result)

if __name__ == "__main__":
    app.debug = True
    app.run()
