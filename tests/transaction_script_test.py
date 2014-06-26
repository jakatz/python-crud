from ..rps import transaction_script
TransactionScript = transaction_script.TransactionScript
# from rps import TransactionScript
import unittest as unittest

class TransactionScriptTest(unittest.TestCase):
  def test(self):
    self.assertEqual(TransactionScript().run(), "hello")

def main():
  unittest.main()

if __name__ == '__main__':
  main()
