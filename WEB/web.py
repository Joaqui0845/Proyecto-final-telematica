from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'container2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

# Ruta para la página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Verificar si las credenciales son correctas
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # Redirigir al usuario a otra ruta específica
            return redirect(url_for('dashboard'))
        else:
            # Mostrar un mensaje de error
            return render_template('login.html', error='Credenciales incorrectas')

    return render_template('login.html')

# Ruta para el registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Insertar el nuevo usuario en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cur.close()

        # Redirigir al usuario a la página de login
        return redirect(url_for('login'))

    return render_template('register.html')



# Ruta para el dashboard
### Modificar si se corre dentro de un entorno de nube ###
@app.route('/dashboard')
def dashboard():
    return redirect('http://localhost:5600/?password=123456')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)