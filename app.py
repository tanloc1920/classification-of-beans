from flask import Flask, render_template, request
import numpy as np
import model

app = Flask(__name__,template_folder="template")

@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST' , 'GET'])
def home():
    if request.method == 'POST':
        area = request.form['a']
        perimeter = request.form['b']
        major = request.form['c']
        minor = request.form['d']
        aspect = request.form['e']
        eccentricity = request.form['f']
        convex = request.form['g']
        equiv = request.form['h']
        extent = request.form['i']
        solidity = request.form['j']
        roundness = request.form['k']
        compactness = request.form['l']
        shape1 = request.form['m']
        shape2 = request.form['n']
        shape3 = request.form['o']
        shape4 = request.form['p']
        arr = np.array([[area, perimeter, major, minor, aspect, eccentricity, convex, equiv, extent, solidity, roundness, compactness, shape1, shape2, shape3, shape4]])
        trained_model = model.training_model()
        pred = trained_model.predict(arr)

        seker = 'seker'
        barbunya = 'barbunya'
        bombay = 'bombay'
        cali = 'cali'
        dermosan = 'dermosan'
        horoz = 'Horoz'
        sira = 'Sira'

        if pred == 0:
            return render_template('id1.html',seker=seker)
        elif pred == 1:
            return render_template('id2.html',barbunya=barbunya)
        elif pred == 2:
            return render_template('id3.html',bombay=bombay)
        elif pred == 3:
            return render_template('id4.html',cali=cali)
        elif pred == 4:
            return render_template('id5.html',horoz=horoz)
        elif pred == 5:
            return render_template('id6.html',sira=sira)
        else:
            return render_template('id7.html',dermosan=dermosan)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)