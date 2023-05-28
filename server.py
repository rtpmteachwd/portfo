
import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        choice1 = data.get('choice1', '')  # Provide a default value if 'choice1' key is missing
        choice2 = data.get('choice2', '')
        choice3 = data.get('choice3', '')
        choice4 = data.get('choice4', '')
        choice5 = data.get('choice5', '')
        choice6 = data.get('choice6', '')
        name = data.get('name', '')
        email = data.get('email', '')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([choice1, choice2, choice3, choice4, choice5, choice6, name, email])
        
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # with open('database.txt', 'a') as f:
            #     f.write(str(data) + '\n')  
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else: 
        return 'Something went wrong. Try again!!'
