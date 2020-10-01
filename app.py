from flask import Flask, render_template, redirect, request
import uuid
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('json_todo_data.txt') as json_store:
        data = json.load(json_store)
        task_list_with_ident = list(data.values())
    # return '<h1>HELLO<h1>'
    return render_template('index.html', task_data=task_list_with_ident)

@app.route('/about')
def about():
    return 'My Page'
    # return render_template('about.html')

@app.route('/add-task', methods=['POST'])
def add_task():
    data = {}

    with open('json_todo_data.txt', 'r') as json_store:
        data = json.load(json_store)

    task = request.form['content']
    uuid_string = str(uuid.uuid4())
    data[uuid_string] = {
        'identifier': uuid_string,
        'content': task,
    }
    json_data = json.dumps(data)

    with open('json_todo_data.txt', 'w') as json_store:

        json_store.write(json_data)

    return redirect('/')

@app.route('/delete-task/<string:task_identifier>/', methods=['POST'])
def delete_task(task_identifier):
    data = {}

    with open('json_todo_data.txt', 'r') as json_store:
        data = json.load(json_store)

    data.pop(task_identifier)
    json_data = json.dumps(data)

    with open('json_todo_data.txt', 'w') as json_store:

        json_store.write(json_data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)