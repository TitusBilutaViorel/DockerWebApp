from flask import Flask
import psycopg2

#creaza o instanta a aplicatiei
app = Flask(__name__)

#configureaza conexiunea la baza de date
db_config = {
    'host': 'db',               #numele serviciului PostgreSQL din Docker Compose
    'database': 'postgres',     #numele bazei de date
    'user': 'titusbiluta',     
    'password': 'admin'
}

#ruta pentru aplicatia Flask (cand se acceseaza pagina aplicatiei, URL-ul, se apeleaza functia)
@app.route('/')
def hello():
#incercare conectare la baza de date
    try:
        #contectare la baza de date PostgreSQL folosind parametrii din db_config
        conn = psycopg2.connect(**db_config)
	#creaza un cursor pentru a executa comenzi SQL pe baza de date
        cursor = conn.cursor()
	#verifica daca conexiunea este activa
        cursor.execute('SELECT version();')
	#obtine primul rand de rezultate din interogare
        db_version = cursor.fetchone()
        return f"Data base is connected: {db_version}"
    except Exception as e:
        return f"The connection to the database cannot be established: {e}"
    finally:
        if conn:
            conn.close()  #inchide conexiunea la baza de date

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
