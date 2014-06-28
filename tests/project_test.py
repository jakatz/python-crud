from ..rps.project import Project

import unittest as unittest

class ProjectTest(unittest.TestCase):
  def create_project_test(self):
    project = Project("MakerSquare", 5)
    self.assertIsInstance(project, Project)
    self.assertEquals(project.name, "MakerSquare")
    self.assertEquals(project.id, 5)