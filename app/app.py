from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # Lógica para obtener los detalles del proyecto con el ID dado
    # Por ahora, usaremos datos ficticios
    project = {
        'id': project_id,
        'title': 'Proyecto de ejemplo',
        # Otros detalles del proyecto...
    }
    return render_template('project_detail.html', project=project)

@app.route('/dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/landing')
def landing_page():
    return render_template('landing_page.html')

if __name__ == '__main__':
    app.run(debug=True)
