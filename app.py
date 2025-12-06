# app.py
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON деректерін оқитын функция
def load_university_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # Хабарламаны аударамыз
        print("Error: data.json file not found! The project will not function.") 
        return []

# Негізгі Route
@app.route('/', methods=['GET', 'POST'])
def index():
    all_universities = load_university_data()
    selected_unis = []
    
    if request.method == 'POST':
        selected_ids = request.form.getlist('selected_unis')
        selected_unis = [uni for uni in all_universities if uni['id'] in selected_ids]
    elif all_universities:
        selected_unis = all_universities  

    return render_template(
        'index.html',
        project_name="FutureCampus", 
        universities=all_universities, 
        selected_unis=selected_unis    
    )

if __name__ == '__main__':
    app.run(debug=True)