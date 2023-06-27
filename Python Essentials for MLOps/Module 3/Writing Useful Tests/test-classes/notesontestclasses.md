Notes on Test Classes

def setup(self) will run before every single test in a test class

def teardown(self) will run after every single test in a test class regardless if it passes, fails, has a bug etc

def setup_class(cls) will run once before every test in the test class.
take note "cls" is used instead of "self"

def teardown_class(cls) will run once after all the tests run in a given (test) class. take note "cls" is used instead of "self"
