import unittest
import estherj
import StringIO
import subprocess

class TestEstherJ(unittest.TestCase):
    simpleInputPath = 'fixtures/simple.cson'
    simpleExpectedOutput = '{"foo": "Bar"}'
    complexInputPath = 'fixtures/complex.cson'
    complexExpectedOutput = '{"array": [1, 2, 3], "object": {"bux": "poi", "foo": "bar"}}'

    def testSimpleConversion(self):
        self._callWith(self.simpleInputPath, self.simpleExpectedOutput)

    def testComplexConversion(self):
        self._callWith(self.complexInputPath, self.complexExpectedOutput)

    def testSimpleShellConversion(self):
        self._callUsingShellWith(self.simpleInputPath, self.simpleExpectedOutput)

    def testComplexShellConversion(self):
        self._callUsingShellWith(self.complexInputPath, self.complexExpectedOutput)

    def testShellErrorWithoutFilepath(self):
        child = subprocess.Popen(["python", "estherj.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        child.communicate()
        self.assertNotEquals(child.returncode, 0)

    def _callUsingShellWith(self, inputPath, expectedOutput):
        output = subprocess.check_output(["python", "estherj.py", inputPath])

        self.assertEquals(output, expectedOutput)

    def _callWith(self, inputPath, expectedOutput):
        with open(inputPath, 'r') as inputFile:
            output = StringIO.StringIO()
            estherj.convert(inputFile, output)

        outputText = output.getvalue()

        self.assertEquals(outputText, expectedOutput)


if __name__ == '__main__':
    unittest.main()
