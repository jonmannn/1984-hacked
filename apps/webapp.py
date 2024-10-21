from flask import Flask, request, render_template_string
from flask_basicauth import BasicAuth
import os

# Create Flask application
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'winston.smith@newspeakprinting.com'
app.config['BASIC_AUTH_PASSWORD'] = 'Julia1984!'

basic_auth = BasicAuth(app)

# Define a route for the homepage
@app.route('/', methods=['GET', 'POST'])
@basic_auth.required
def index():
    ping_result = ""
    if request.method == 'POST':
        # Address received from user
        address = request.form['address']

        # Number of pings to send, default is 3 if not specified
        ping_count = request.form.get('ping_count', '3')

        command = "ping -c {} {}".format(ping_count, address)
        print(command)
        # Execute the ping command and get the result
        ping_result = os.popen(command).read()
        print(ping_result)

    # Display the HTML form and ping results
    return render_template_string('''
  <!DOCTYPE html>
<html>
<head>
    <title>Printer Tester</title>
    <style>
        body {
            font-family: monospace;
            margin: 0;
            background-color: #ADD8E6; /* Light gray background */
        }

        .container {
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15); /* Soft shadow */
            background-color: #fff; /* White background */
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        input[type="text"],
        select {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
            width: 200px;
        }

        input[type="submit"] {
            background-color: #4CAF50; /* Green background */
            color: white;
            font-family: monospace;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        pre {
            margin-top: 20px;
            padding: 10px;
            background-color: #eee; /* Light gray background */
            border-radius: 5px;
            overflow-x: auto; /* Enable horizontal scrolling */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Site Tester</h1>
        <h3 style="text-align:center;">Input the IP address of a flatbed printer to verify operation.</h3>
        <form method="post">
            Client: <input type="text" name="address">
            <input type="submit" value="Send Ping">
        </form>
        <pre>{{ ping_result }}</pre>
    </div>
</body>
</html>

    ''', ping_result=ping_result)

# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)