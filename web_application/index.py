from flask import Flask, render_template, request
import pickle
import numpy as np

# setup flask
app = Flask(__name__)

def prediction(lst,text):
   
    filename = 'model/{}.pickle'.format(text)
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    result = np.exp(pred_value)
    return result



@app.route('/', methods=['POST', 'GET'])
def index():
   
    pred_value = 0
    if request.method == 'POST':
        type = request.form['type']
        carat = request.form['carat']
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depthPre = request.form['depthPre']
        table = request.form['table']
        length = request.form['length']
        width = request.form['width']
        depth = request.form['depth']
        
        diamonds_list = []
        text = ''

        diamonds_list.append(float(carat))
        diamonds_list.append(int(cut))
        diamonds_list.append(int(color))
        diamonds_list.append(int(clarity))

        diamonds_list.append(float(depthPre))
        diamonds_list.append(float(table))
        diamonds_list.append(float(length))
        diamonds_list.append(float(width))
        diamonds_list.append(float(depth))
        
        if int(type) == 1:
            text = 'random_forest'
        elif int(type) == 2:
            text = 'decision_tree'
        elif int(type) == 3:
            text = 'svr_regressor'
        elif int(type) == 4:
            text = 'linear_regressor'
             

        pred_value = prediction(diamonds_list,text)
        pred_value = np.round(pred_value[0],2)

        # convert text value to capital letter and remove underscore
        text = text.replace('_',' ').title()

    return render_template('diamond.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)
