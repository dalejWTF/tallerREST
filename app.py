from flask import Flask, jsonify, request

app = Flask(__name__)

from students import students

# Testeo de ruta
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# metodo GET de estudiantes
@app.route('/students')
def getStudets():
    return jsonify({'students': students})


@app.route('/students/<int:students_id>')
def getStudentsId(students_id):
    studentsFound = [
        students for students in students if students['id'] == students_id]
    if (len(studentsFound) > 0):
        return jsonify({'students': studentsFound[0]})
    return jsonify({'message': 'students Not found'})


@app.route('/students/<string:students_name>')
def getStudents(students_name):
    studentsFound = [
        students for students in students if students['name'] == students_name.lower() or students['name'] == students_name.upper() or students['name'] == students_name.capitalize()]
    if (len(studentsFound) > 0):
        return jsonify({'students': studentsFound})
    return jsonify({'message': 'students Not found'})

# Metodo POST
@app.route('/students', methods=['POST'])
def addStudents():
    new_students = {
        'id': request.json['id'],
        'name': request.json['name'],
        'mail': request.json['mail'],
        'age': request.json['age']
    }
    students.append(new_students)
    return jsonify({'students': students})

# Metodo PUT
@app.route('/students/<int:students_id>', methods=['PUT'])
def editStudents(students_id):
    studentsFound = [students for students in students if students['id'] == students_id]
    if (len(studentsFound) > 0):
        studentsFound[0]['id'] = request.json['id']
        studentsFound[0]['name'] = request.json['name']
        studentsFound[0]['mail'] = request.json['mail']
        studentsFound[0]['age'] = request.json['age']
        return jsonify({
            'message': 'students Updated',
            'students': studentsFound[0]
        })
    return jsonify({'message': 'students Not found'})

# metodo DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def deleteStudents(id):
    studentsFound = [students for students in students if students['id'] == id]
    if len(studentsFound) > 0:
        students.remove(studentsFound[0])
        return jsonify({
            'message': 'students Deleted',
            'students': students
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)
