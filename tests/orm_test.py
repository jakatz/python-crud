from ..rps import orm
from ..rps import project
ORM = orm.ORM
Project = project.Project

import unittest as unittest

class ORMTest(unittest.TestCase):
  def add_project_test(self):
    project = ORM().add_project()
    self.assertIsInstance(project, Project)


def main():
  unittest.main()

if __name__ == '__main__':
  main()
