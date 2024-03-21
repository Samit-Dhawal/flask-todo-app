from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#sample todo list
todos = []

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        todos.append(task)
    return render_template('index.html',todos=todos)

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(todos):
        del todos[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)