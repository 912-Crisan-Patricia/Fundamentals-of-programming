import unittest
from service import Service
from repository import Repo, File


class Test(unittest.TestCase):
    def setUp(self):
        self.repo = File()
        self.service = Service(self.repo)
        return super().setUp()

    def tearDown(self):
        return super.tearDown(self)

    def test_add(self):
        count = len(self.repo.get_all())
        self.service.add("hello world")
        self.assertEqual(len(self.repo.get_all()), count + 1)

    def test_get_random(self):
        self.repo.add("hello world1")
        self.repo.add("hello world2")
        random_sentence = self.service.get_random()
        self.assertIn(random_sentence, self.repo.get_all())

    def test_partialdisplay(self):
        sentence = "hello world"
        display = self.service.partialdisplay(sentence)
        self.assertEqual(display, ['h', '_', '_', '_', 'o', ' ', 'w', '_', '_', '_', 'd'])

    def test_play(self):
        sentence = "hello world"
        display = ['h', '_', '_', '_', 'o', ' ', 'w', '_', '_', '_', 'd']
        display = self.service.play('l', display, sentence)
        self.assertEqual(display, ['h', '_', 'l', 'l', 'o', ' ', 'w', '_', '_', 'l', 'd'])

unittest.main()