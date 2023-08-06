
import unittest
from os.path import normpath

from yaml_walker.__main__ import run_cli, parse


class Test_Ypath(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._path = normpath(r'./example.yaml')

    def test_simple_ypath(self):
        pattern = 'node.nd_1.data'
        result = run_cli([pattern, self._path])
        print(f"Result: {result}")

    def test_ypath_comparer(self):
        pattern = 'node.nd_1.data[id=2]'
        result = run_cli([pattern, self._path])
        print(f"Result: {result}")

    def test_ypath_comparer_with_gt(self):
        pattern = 'node.nd_2.data[id>=2]'
        result = run_cli([pattern, self._path])
        print(f"Result: {result}")

    def test_ypath_comparer_with_sub_node(self):
        pattern = 'node.nd_1.data[id=2]sub_data'
        result = run_cli([pattern, self._path])
        print(f"Result: {result}")

    def test_ypath_comparer_with_regex(self):
        pattern = 'node.nd_+'
        result = run_cli([pattern, self._path])
        print(f"Result: {result}")


class Test_YamlDict(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._path = r'.\example.yaml'

    def test_simple(self):
        y_dict = parse(self._path)
        result = y_dict.node.nd_1.data
        self.assertNotEqual(result, "Empty!!!")
        print(f"Result: {result}")

    def test_comparer(self):
        y_dict = parse(self._path)
        result = y_dict.node.nd_1.data['id=2']
        self.assertNotEqual(result, "Empty!!!")
        print(f"Result: {result}")

    def test_comparer_with_gt(self):
        y_dict = parse(self._path)
        result = y_dict.node.nd_1.data['id>2']
        self.assertNotEqual(result, "Empty!!!")
        print(f"Result: {result}")

    def test_comparer_with_sub_node(self):
        y_dict = parse(self._path)
        result = y_dict.node.nd_1.data['id=2'].sub_data
        self.assertNotEqual(result, "Empty!!!")
        print(f"Result: {result}")


if __name__ == '__main__':
    unittest.main()
