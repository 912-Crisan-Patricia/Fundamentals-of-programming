import unittest
from service import Service
from repo import Repo

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo=Repo("troute.txt","tbus.txt")
        self.service=Service(self.repo)
        return super().setUp()

    def tearDown(self) -> None:
        return super.tearDown(self)

    def test(self):
        returned= self.service.getBusMilage()
        self.assertEqual(len(returned),3)

unittest.main()