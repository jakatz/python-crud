from ..rps import add_project
from ..rps import project
AddProject = add_project.AddProject
Project = project.Project

import unittest as unittest

class AddProjectTest(unittest.TestCase):
  def add_project_test(self):
    project = AddProject().run()
    self.assertIsInstance(project, Project)

def main():
  unittest.main()

if __name__ == '__main__':
  main()
