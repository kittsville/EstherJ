import unittest
import estherj
import StringIO
import subprocess

class TestEstherJ(unittest.TestCase):
    simpleInput = 'foo:"Bar"'
    simpleExpectedOutput = '{"foo": "Bar"}'
    complexInput = """
# A comment

array: [
1
2
3
]
object:
    foo: 'bar'
    bux: 'poi'
"""
    complexExpectedOutput = '{"array": [1, 2, 3], "object": {"bux": "poi", "foo": "bar"}}'

    def testSimpleConversion(self):
        self._callWith(self.simpleInput, self.simpleExpectedOutput)

    def testComplexConversion(self):
        self._callWith(self.complexInput, self.complexExpectedOutput)

    def testSimpleShellConversion(self):
        self._callUsingShellWith(self.simpleInput, self.simpleExpectedOutput)

    def testComplexShellConversion(self):
        self._callUsingShellWith(self.complexInput, self.complexExpectedOutput)

    def _callUsingShellWith(self, inputText, expectedOutput):
        p = subprocess.Popen(["python", "estherj.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.stdin.write(inputText.encode('ASCII')) # Convert to byte object
        output = p.communicate()[0]
        p.stdin.close()

        self.assertEquals(output, expectedOutput)

    def _callWith(self, inputText, expectedOutput):
        input  = StringIO.StringIO(inputText)
        output = StringIO.StringIO()

        estherj.convert(input, output)

        outputText = output.getvalue()

        self.assertEquals(outputText, expectedOutput)


if __name__ == '__main__':
    unittest.main()
