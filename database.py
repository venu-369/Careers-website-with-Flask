from sqlalchemy import create_engine, text
import os, json

db_connection_String = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_String,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def convert_value(value):
  if isinstance(value, bool):
    return value
  elif isinstance(value, int):
    return value
  elif isinstance(value, float):
    return value
  elif isinstance(value, str):
    return value
  elif value is None:
    return value
  else:
    return str(value)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      row_list = list(row)
      row_dict = {
        col_name: convert_value(value)
        for col_name, value in zip(result.keys(), row_list)
      }
      jobs.append(row_dict)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"),
                          {'id': id})
    row = result.first()
    if row is None:
      return None
    else:
      row_dict = {
        col_name: convert_value(value)
        for col_name, value in zip(result.keys(), row)
      }
      return row_dict


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'work_experience': data['work_experience'],
        'resume_url': data['resume_url']
      })
