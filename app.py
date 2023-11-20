from flask import *
from mysql import connector

app = Flask(__name__)

#open connection
db = connector.connect(
    host    = 'kil-thedb.database.windows.net',
    user    = 'lucy',
    passwd  = 'Darklatias2000',
    database= 'dbkiller'
)
if db.is_connected():
    print('''
    Lord knows and I think I know it too sometimes
    Every time and they reachin' out for what's mine
    I've been awake for days
    So we out living life in the night
    Pray to god, man I hope I don't die
    I've been awake for days
    So we out living life in the night
    Pray to god, man I hope I don't die in the night''')
@app.route('/admin')
def admin():
    cursor = db.cursor()
    cursor.execute('select * from students')
    result = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', hasil = result)

@app.route('/')
def main():
    cursor = db.cursor()
    cursor.execute('select * from students')
    result = cursor.fetchall()
    cursor.close()
    return render_template('main.html', hasil = result)
    
@app.route('/tambah/')
def tambah_data():
    return render_template('tambah.html')

@app.route('/proses_tambah/', methods=['POST'])
def proses_tambah():
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    jurusan = request.form['prodi']
    daerah = request.form['daerah']
    cur = db.cursor()
    cur.execute('INSERT INTO students (nim, nama, jk, prodi, asal) VALUES (%s, %s, %s, %s, %s)', (nim, nama, jk, jurusan, daerah))
    db.commit()
    return redirect(url_for('admin'))

@app.route('/edit/<id>', methods=['GET','POST'])
def ubah_data(id):
    cur = db.cursor()
    cur.execute('select * from students where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('edit.html', hasil=res)

@app.route('/editing_data/', methods=['POST'])
def proses_ubah():
    idid = request.form['id0']
    formid = request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    prodi = request.form['prodi']
    asal = request.form['daerah']
    cur = db.cursor()
    sql = "UPDATE students SET id=%s, nim=%s, nama=%s, jk=%s, prodi=%s, asal=%s WHERE id=%s"
    value = (formid, nim, nama, jk, prodi, asal, idid)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('admin'))

@app.route('/hapus/<id>', methods=['GET'])
def hapus_data(id):
    cur = db.cursor()
    cur.execute('DELETE from students where id=%s', (id,))
    db.commit()
    return redirect(url_for('admin'))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' port=)