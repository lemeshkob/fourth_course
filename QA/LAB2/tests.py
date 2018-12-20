from unittest import TestCase, mock
from unittest.mock import patch
import unittest
from exception_manager import ExceptionManager, MyServerHandler

CRITICAL_COUNT = 1
NON_CRITICAL_COUNT = 1
SERVER_RETURN_TRUE = True
SERVER_RETURN_FALSE = False

class TestIsChecked(TestCase):

    def setUp(self):
        self.e_manager = ExceptionManager()
        print(self._testMethodName)

    def tearDown(self):
        print("\n============ENDED============\n")
    
    def test_exception_manager_is_critical_method_positive(self):
        e = TypeError()
        with patch('file_handler.MyFileHandler.file_handler') as mocked_file_handler:
            mocked_file_handler.return_value = ['TypeError', 'AttributeError']
            self.assertTrue(self.e_manager.is_critical(e))
            print("====Exception is critical====")

    def test_exception_manager_is_critical_method_negative(self):
        e = IndentationError()
        with patch('file_handler.MyFileHandler.file_handler') as mocked_file_handler:
            mocked_file_handler.return_value = ['TypeError', 'AttributeError']
            self.assertFalse(self.e_manager.is_critical(e))
            print("====Exception is not critical====")

    def test_handler_manager_positive(self):
        e = TypeError()
        with patch('exception_manager.MyServerHandler.is_checked') as mocked_server_check:
            mocked_server_check.return_value = True
            self.e_manager.handle_manager(e)
            self.assertEqual(SERVER_RETURN_TRUE, mocked_server_check())
            print("====Server has returned True value====")
            self.assertEqual(CRITICAL_COUNT, self.e_manager.is_critical_count)
            print("====Exception is critical====")

    def test_handler_manager_negative(self):
        e = TypeError()
        with patch('exception_manager.MyServerHandler.is_checked') as mocked_server_check:
            mocked_server_check.return_value = False
            self.e_manager.handle_manager(e)
            self.assertEqual(SERVER_RETURN_FALSE, mocked_server_check())
            print("====Server has returned False value====")
            self.assertEqual(NON_CRITICAL_COUNT, self.e_manager.is_not_critical_count)
            print("====Exception is not critical====")

if __name__ == '__main__':
    unittest.main()

