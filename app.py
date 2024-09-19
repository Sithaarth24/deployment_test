from flask import Flask, request, render_template_string

app = Flask(__name__)

# Template for the input form
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Form</title>
</head>
<body>
    <h1>Input Form</h1>
    <form action="/display" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

# Template for displaying the result
result_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Display Result</title>
</head>
<body>
    <h1>Display Result</h1>
    <p>Hello, {{ name }}!</p>
    <a href="/">Go back</a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(form_template)

@app.route('/display', methods=['POST'])
def display():
    name = request.form.get('name')
    return render_template_string(result_template, name=name)

if __name__ == '__main__':
    app.run(debug=True)
