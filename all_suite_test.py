import unittest

from unittest.loader import makeSuite

from test_cases.fill_in_add_player_form import TestAddPlayerForm
from test_cases.login_to_the_syste import TestLoginPage
from test_cases.framework import Test


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayerForm))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(Test))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
