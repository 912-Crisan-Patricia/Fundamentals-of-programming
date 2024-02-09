import unittest
from domain import Reservation
from repository import Repository, Repository_rooms
from service import Service

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repo = Repository()
        self.reservation1 = Reservation(1, 1, "John Doe", 2, 1, 2, 3, 4)
        self.reservation2 = Reservation(2, 5, "Jane Smith", 3, 2, 3, 4, 5)

    def test_add_and_get_reservation(self):
        self.repo.add(self.reservation1)
        self.repo.add(self.reservation2)
        self.assertEqual(len(self.repo.get()), 2)

    def test_delete_reservation(self):
        self.repo.add(self.reservation1)
        self.repo.add(self.reservation2)
        self.repo.delete(self.reservation1)
        self.assertEqual(len(self.repo.get()), 1)


class TestService(unittest.TestCase):
    def setUp(self):
        self.rooms_repo = Repository_rooms()  # Example: Replace with appropriate repository class
        self.reservations_repo = Repository()
        self.service = Service(self.rooms_repo, self.reservations_repo)
        self.reservation1 = Reservation(1, 101, "John Doe", 2, 1, 2, 3, 4)

    def test_create_reservation(self):
        result = self.service.create("John Doe", 101, 2, 1, 2, 3, 4)
        self.assertEqual(len(self.reservations_repo.get()), 0)
        self.assertEqual(result,0)


if __name__ == '__main__':
    unittest.main()