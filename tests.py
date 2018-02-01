import unittest
import estherj
import StringIO

class TestEstherJ(unittest.TestCase):
    def testSimpleConversion(self):
        input          = 'foo:"Bar"'
        output         = StringIO.StringIO()
        expectedOutput = '{"foo": "Bar"}'

        estherj.convert(input, output)

        outputText = output.getvalue()

        self.assertEquals(outputText, expectedOutput)


if __name__ == '__main__':
    unittest.main()
