class TestCase:
    def __init__(self, name):
        print("TestCase1")
        print("name= ", name)
        self.name = name

    def setUp(self):
        print("TestCase2")
        pass

    def run(self):
        print("TestCase3")
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        print("WasRun1")
        self.wasRun= None
        TestCase.__init__(self, name)

    def testMethod(self):
        print("WasRun2")
        self.wasRun = 1

    def setUp(self):
        print("WasRun3")
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def setUp(self):
        print("TestCaseTest1")
        self.test = WasRun("testMethod")

    def testRunning(self):
        print("TestCaseTest2")
        self.test.run()
        assert (self.test.wasRun)

    def testSetUp(self):
        print("TestCaseTest3")
        self.test.run()
        assert (self.test.wasSetUp)

TestCaseTest("testRunning").run()
print("------"*50)
TestCaseTest("testSetUp").run()