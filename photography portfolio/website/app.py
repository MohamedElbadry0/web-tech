from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(f"Received message from {name} ({email}): {message}")
        
        return render_template('contact_success.html', name=name)  

@app.route('/portfolio')
def portfolio():
    # Add any data or logic needed for your portfolio page
    return render_template('portfolio.html')

@app.route('/shop')
def shop():
    # Add logic to fetch data or perform operations related to the shop
    # For example, fetching items to display in the shop page
    items = [
        {'id': 1, 'name': 'Item 1', 'price': 10.0},
        {'id': 2, 'name': 'Item 2', 'price': 15.0},
        # Add more items as needed
    ]
    return render_template('shop.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

    