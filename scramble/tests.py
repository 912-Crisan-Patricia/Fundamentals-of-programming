import unittest
from service import Service
from repository import Repo,File

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.repo=File()
        self.service=Service(self.repo)
        return super().setUp()

    def tearDown(self) -> None:
        return super.tearDown(self)

    def test_get_random(self):
        self.repo.add("hello world1")
        self.repo.add("hello world2")
        random_sentence = self.service.get_random()
        self.assertIn(random_sentence, self.repo.get_all())
    def test_shuffle_sentence(self):
        sentence = "hello world"
        shuffled = self.service.shuffle_sentence(sentence)
        self.assertNotEqual(sentence, shuffled)

    def test_swap(self):
        sentence = "hello world"
        shuffled = self.service.shuffle_sentence(sentence)
        score = self.service.get_score(sentence)
        self.service.swap(0, 0, 0, 1, shuffled)
        self.assertEqual(score, self.service.get_score(shuffled))