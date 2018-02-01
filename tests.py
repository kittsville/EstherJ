import unittest
import estherj
import StringIO

class TestEstherJ(unittest.TestCase):
    def testSimpleConversion(self):
        self._testWith('foo:"Bar"', '{"foo": "Bar"}')

    def testComplexConversion(self):
        input = """
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
        expectedOutput = '{"array": [1, 2, 3], "object": {"bux": "poi", "foo": "bar"}}'

        self._testWith(input, expectedOutput)

    def _testWith(self, input, expectedOutput):
            output         = StringIO.StringIO()

            estherj.convert(input, output)

            outputText = output.getvalue()

            self.assertEquals(outputText, expectedOutput)


if __name__ == '__main__':
    unittest.main()
