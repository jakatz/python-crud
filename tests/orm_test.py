from ..rps import orm
from ..rps import project
ORM = orm.ORM
Project = project.Project

import unittest as unittest

class ORMTest(unittest.TestCase):
  def add_project_test(self):
    project = ORM().add_project("MakerSquare")
    self.assertIsInstance(project, Project)
    self.assertEquals(project.name, "MakerSquare")
    self.assertIsInstance(project.id, int)

  # def get_project_test(self):
  #   project = ORM().add_project("MakerSquare")
  #   project2 = ORM().get_project(project.id)
  #   self.assertEquals(project.id, project2.id)
  #   self.assertEquals(project.name, project2.name)