from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)

# configure db
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # fetch from data
        userDetails = request.form
        naam = userDetails['naam']
        achternaam = userDetails['achternaam']
        email = userDetails['email']
        Dag = userDetails['Dag']
        behandeling = userDetails['behandeling']
        print(naam, achternaam, email, behandeling)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hairstudio(Voornaam, Achternaam, email, Dag, Behandeling)VALUES(%s, %s, %s, %s, %s)",(naam,achternaam,email,Dag,behandeling))
        mysql.connection.commit()
        cur.close()
        return render_template('bevesteging.html')
    return render_template('probeer.html')


if __name__ == '__main__':
    app.run(debug=True)
