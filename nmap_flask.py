from flask import Flask, render_template, request
from test_nmap import scan_ip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('nmap_search.html')

@app.route('/nmap_answer', methods=['GET', 'POST'])
def nmap_answer():
    ip = request.form['ip']
    result = scan_ip(ip)
    return render_template('nmap_answer.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
