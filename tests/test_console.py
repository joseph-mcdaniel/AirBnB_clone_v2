#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
import models
from datetime import datetime
import console
import inspect

State = models.state.State
User = models.user.User
HBNBCommand = console.HBNBCommand
FS = console.FS


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    all_funcs = inspect.getmembers(console.HBNBCommand, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCommand interpreter for Holberton AirBnB project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Command inerpreter class'
        actual = HBNBCommand.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in console file"""
        AF = TestHBNBCommandDocs.all_funcs
        for f in AF:
            if "_HBNBCommand_" in f[0]:
                self.assertTrue(len(f[1].__doc__) > 1)


class TestHBNBCommandfunc(unittest.TestCase):
    """Test instantiation of CLI with tests for all other functions"""

    cli = HBNBCommand()
    obj = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.. Testing All other Functions ..')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new State object: ', end='')
        TestHBNBCommandfunc.cli.do_create('State')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            TestHBNBCommandfunc.obj = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandfunc.cli
        self.obj = TestHBNBCommandfunc.obj

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, State)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        self.CLI.do_update('State {} name "California"'.format(self.obj.id))
        actual = self.obj.name
        expected = 'California'
        self.assertEqual(expected, actual)

    def test_destroy(self):
        """... checks if object can be destroyed"""
        self.CLI.do_destroy('State {}'.format(self.obj.id))
        try:
            self.obj
            self.assertTrue(False)
        except:
            self.assertIsNone(None)


class TestHBNBCommandfunc2(unittest.TestCase):
    """Test instantiation of CLI with tests for .function() notation"""

    cli = HBNBCommand()
    obj = None
    obj2 = None

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('... Tests .function() noation ...')
        print('..... For HBNBCommand Class .....')
        print('.................................\n\n')
        FS.delete_all()
        print('...creating new User object: ', end='')
        TestHBNBCommandfunc2.cli.do_User('.create()')
        print('...creating new User object: ', end='')
        TestHBNBCommandfunc2.cli.do_User('.create()')
        print('')
        fs_o = FS.all()
        for v in fs_o.values():
            if not TestHBNBCommandfunc2.obj:
                TestHBNBCommandfunc2.obj = v
            else:
                TestHBNBCommandfunc2.obj2 = v

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBCommandfunc2.cli
        self.obj = TestHBNBCommandfunc2.obj
        self.obj2 = TestHBNBCommandfunc2.obj2

    def test_instantiation(self):
        """... checks if HBNBCommand is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class User with attributes"""
        self.assertIsInstance(self.obj, User)

    def test_attr_update(self):
        """... checks if proper parameter for name was created"""
        self.CLI.do_User('.update("{}", "first_name", '
                         '"Mongo")'.format(self.obj.id))
        actual = self.obj.first_name
        expected = "Mongo"
        self.assertEqual(expected, actual)

    def test_update_dict(self):
        """... checks if proper parameters created with dict"""
        self.CLI.do_User('.update("{}", {{"last_name": "Nginx", '
                         '"age": 89}})'.format(self.obj.id))
        actual = self.obj.last_name
        expected = 'Nginx'
        self.assertEqual(expected, actual)
        actual = self.obj.age
        expected = 89
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_reupdate(self):
        """... checks if attribute can be reupdated"""
        self.CLI.do_User('.update("{}", "age", 55)'.format(self.obj.id))
        actual = self.obj.age
        expected = 55
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_destroy(self):
        """... checks if object can be destroyed"""
        self.CLI.do_destroy('User {}'.format(self.obj2.id))
        try:
            self.obj2
            self.assertTrue(False)
        except:
            self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main
