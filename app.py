from flask import Flask, render_template, request, jsonify
import json
from collections import defaultdict

app = Flask(__name__)

# Sample student data for 9-Anadolu A class
STUDENTS = [
    "Aaliyah", "Aiden", "Amelia", "Benjamin", "Chloe", "Daniel", "Ella", "Finn",
    "Grace", "Henry", "Isabella", "Jack", "Kylie", "Liam", "Maya", "Noah",
    "Olivia", "Parker", "Quinn", "Ruby", "Samuel", "Taylor", "Uma", "Victor",
    "Willow", "Xavier", "Yasmin", "Zoe"
]

def group_students_alphabetically(students):
    """Group students by their first letter"""
    grouped = defaultdict(list)
    for student in sorted(students):
        first_letter = student[0].upper()
        grouped[first_letter].append(student)
    return dict(grouped)

def get_avatar_color(letter):
    """Get color class for avatar based on first letter"""
    colors = {
        'A': 'primary', 'B': 'emerald', 'C': 'rose', 'D': 'fuchsia',
        'E': 'sky', 'F': 'indigo', 'G': 'purple', 'H': 'pink',
        'I': 'amber', 'J': 'lime', 'K': 'teal', 'L': 'cyan',
        'M': 'orange', 'N': 'violet', 'O': 'slate', 'P': 'red',
        'Q': 'yellow', 'R': 'green', 'S': 'blue', 'T': 'indigo',
        'U': 'purple', 'V': 'pink', 'W': 'rose', 'X': 'emerald',
        'Y': 'sky', 'Z': 'amber'
    }
    return colors.get(letter, 'primary')

@app.route('/')
def index():
    """Main route for student directory"""
    grouped_students = group_students_alphabetically(STUDENTS)
    return render_template('index.html', 
                         grouped_students=grouped_students,
                         get_avatar_color=get_avatar_color)

@app.route('/students/<student_name>')
def student_detail(student_name):
    """Student detail page (placeholder)"""
    if student_name in STUDENTS:
        return f"<h1>Student: {student_name}</h1><p>Detail page for {student_name}</p>"
    else:
        return "Student not found", 404

@app.route('/api/search')
def search_students():
    """API endpoint for searching students"""
    query = request.args.get('q', '').lower()
    if not query:
        filtered_students = STUDENTS
    else:
        filtered_students = [s for s in STUDENTS if query in s.lower()]
    
    grouped_students = group_students_alphabetically(filtered_students)
    return jsonify(grouped_students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)