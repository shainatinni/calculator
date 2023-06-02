from flask import Flask, render_template, request

calcu = Flask(__name__)

@calcu.route('/')
def home():
    return render_template('index.html')

@calcu.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operator = request.form['operator']
    
    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 / num2
    else:
        result = "Invalid operator"
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    calcu.run()
