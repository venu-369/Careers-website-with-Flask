from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title': "Data Analyst",
    'location': 'London, Uk',
    'salary': '£500000'
  },
  {
    'id': 2,
    'title': "Data Scientist",
    'location': 'Birmingham, Uk',
    'salary': '£600000'
  },
  {
    'id': 3,
    'title': "Front-end Engineer",
    'location': 'kent, Uk',
    
  },
  {
    'id': 4,
    'title': "Back-end Engineer",
    'location': 'Manchester, Uk',
    'salary': '£700000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="V")


@app.route('/api/jobs')
def list_jobs():
  return jsonify (JOBS)
  

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)