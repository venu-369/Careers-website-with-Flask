from sqlalchemy import create_engine, text
import os

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
