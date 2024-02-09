import unittest
from service import Service
from repo import Repo

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo=Repo("test.txt")
        self.service=Service(self.repo)
        return super().setUp()

    def tearDown(self) -> None:
        return super.tearDown(self)

    def test(self):
        returned= self.service.get_distance("12","13","255")
        self.assertEqual(len(returned),1)

unittest.main()
