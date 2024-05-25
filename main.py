from flask import Flask, render_template

app = Flask(__name__)

lst_main_menu = [{"name": "Strona główna", "url": "/"},
                 {"name": "Dodaj", "url": "/add"},
                 {"name": "Odśwież", "url": "/update"},
                 {"name": "Usuń", "url": "/delete"},
                 {"name": "Pokaż", "url": "/show"}]

@app.route('/')
def index():
    return render_template('index.html', title='Strona główna', lst_main_menu = lst_main_menu)
@app.route('/add')
def add():
    return render_template('add.html', title = 'Dodaj', lst_main_menu = lst_main_menu)

@app.route('/update')
def update():
    return render_template('update.html', title='Odśwież', lst_main_menu = lst_main_menu)

@app.route('/delete')
def delete():
    return render_template('delete.html', title='Usuń', lst_main_menu = lst_main_menu)

@app.route('/show')
def show():
    return render_template('delete.html', title='Pokaż', lst_main_menu = lst_main_menu)

if __name__ == '__main__':
    app.run(debug=True, port=8000)