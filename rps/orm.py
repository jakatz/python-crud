from project import Project
import psycopg2
import pdb

class ORM:
  def __init__(self):
    self._dbAdapter = psycopg2.connect("host='localhost' dbname='py-pm'")
    self._dbAdapter

  def createTables(self):
    cursor = self._dbAdapter.cursor()
    command = """CREATE TABLE IF NOT EXISTS projects(
              id SERIAL PRIMARY KEY,
              name TEXT)"""
    cursor.execute(command)
    self._dbAdapter.commit()
    cursor.close()

  def deleteTables(self):
    cursor = self._dbAdapter.cursor()
    command = "DROP TABLE IF EXISTS projects;"
    cursor.execute(command)
    self._dbAdapter.commit()
    cursor.close()

  def resetTables(self):
    self.deleteTables()
    self.createTables()

  def add_project(self, name):
    cursor = self._dbAdapter.cursor()
    command = """
              INSERT INTO projects(name)
              VALUES('%s') RETURNING *
              """
    cursor.execute(command, (name))
    conn.commit()
    data = cursor.fetchone()
    cursor.close()
    return Project(data[1], data[0])

  def get_project(self, id):
    cursor = self._dbAdapter.cursor()
    command = """
              SELECT * FROM projects
              WHERE id= %d
              """
    cursor.execute(command)
    conn.commit()
    data = cursor.fetchone()
    cursor.close()
    return Project(data[1], data[0])