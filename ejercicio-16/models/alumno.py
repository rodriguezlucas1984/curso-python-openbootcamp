from sqlite3 import connect
from pathlib import Path


class Alumno:
    def __init__(self, id, nombre, apellido) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self) -> str:
        return f'\n\tIdentificación:{self.id}\n\tNombre:{self.nombre}\n\tApellido:{self.apellido}'


def crearTabla():
    cwd = Path(__file__).parent
    conn = connect(cwd.parent / 'db/test.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS alumnos
            ([id] INTEGER PRIMARY KEY, [nombre] TEXT NOT NULL,[apellido] TEXT NOT NULL)
            ''')

    conn.commit()
    cursor.close()
    conn.close()


crearTabla()


class ModelAlumno:

    @staticmethod
    def __ejecutar(texto, parametros):
        cwd = Path(__file__).parent
        conn = connect(cwd.parent / 'db/test.sqlite')
        cursor = conn.cursor()
        cursor.execute(texto, parametros)

        conn.commit()
        count = cursor.rowcount
        cursor.close()
        conn.close()
        return count

    def __consulta(texto, parametros):
        alumnos = ()
        cwd = Path(__file__).parent
        conn = connect(cwd.parent / 'db/test.sqlite')
        cursor = conn.cursor()
        cursor.execute(texto, parametros)

        rows = cursor.fetchall()
        for row in rows:
            alumno = Alumno(row[0], row[1], row[2])
            alumnos = alumnos+(alumno,
                               )
        cursor.close()
        conn.close()
        return alumnos

    @staticmethod
    def __crear(alumno):
        ModelAlumno.__ejecutar('INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?)',
                               (alumno.id, alumno.nombre, alumno.apellido))

    @staticmethod
    def crear(id, nombre, apellido):
        '''
        Crea un alumno con los datos ingresado
        '''
        alumno = Alumno(id, nombre, apellido)
        ModelAlumno.__crear(alumno)

    def obtenerTodos():
        return ModelAlumno.__consulta("SELECT id, nombre, apellido FROM alumnos", ())

    def cantidad() -> int:
        '''
        Devuelve la cantidad de alumnos registrados
        '''
        cwd = Path(__file__).parent
        conn = connect(cwd.parent / 'db/test.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM alumnos')

        row = cursor.fetchone()

        cursor.close()
        conn.close()
        return int(row[0])

    def buscar(filtros={}):
        '''
        Obtiene los alumno que cumple con los filtros ingresados. Posibles filtros 
        {'id':?,'nombre':?,'apellido':?}
        '''
        if filtros == {}:
            return ModelAlumno.obtenerTodos()
        valores = ()
        condiciones = []

        query = "SELECT id,nombre,apellido FROM alumnos WHERE "
        for campo in filtros:
            condiciones.append(f'{campo}=?')
            valores += (filtros[campo],)
        query += " AND ".join(condiciones)
        return ModelAlumno.__consulta(query, valores)

    def eliminar(id):
        '''
        Borra un alumno con el id respectivo
        '''
        return ModelAlumno.__ejecutar('DELETE FROM alumnos WHERE id=?', (id,))
