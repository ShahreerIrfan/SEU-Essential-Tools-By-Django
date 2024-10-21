from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form route (GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        return redirect(url_for('result', name=name, grade=grade))
    return render_template('submit.html')

# Result route
@app.route('/result/<name>/<grade>')
def result(name, grade):
    return f"Student: {name}, Grade: {grade}"

# A simple route for an about page
@app.route('/about')
def about():
    return "<h2>About this Flask App</h2>"

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
