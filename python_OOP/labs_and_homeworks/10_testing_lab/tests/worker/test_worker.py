from unittest import TestCase, main

from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.first_worker = Worker("Worker_1", 1000, 10)

    def test_if_worker_correctly_initialised(self):
        # Test if the worker is initialized with correct name, salary and energy
        self.assertEqual("Worker_1", self.first_worker.name)
        self.assertEqual(1000, self.first_worker.salary)
        self.assertEqual(10, self.first_worker.energy)

    def test_if_worker_energy_increment_after_rest_method(self):
        # Test if the worker's energy is incremented after the rest method is called
        self.first_worker.rest()
        self.assertEqual(11, self.first_worker.energy)

    def test_if_worker_energy_is_zero_and_try_to_work_raises_exception(self):
        # Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.first_worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.first_worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_energy_is_lower_than_zero_and_try_to_work_raises_exception(self):
        # Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.first_worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.first_worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_money_increase_by_his_salary_after_work(self):
        # Test if the worker's money is increased by his salary correctly after the work method is called
        self.first_worker.money = 0
        self.first_worker.work()
        self.assertEqual(1000, self.first_worker.money)

    def test_if_worker_energy_decrease_after_work(self):
        # Test if the worker's energy is decreased after the work method is called
        self.first_worker.energy = 10
        self.first_worker.work()
        self.assertEqual(9, self.first_worker.energy)

    def test_if_worker_get_info_is_correct(self):
        # Test if the get_info method returns the proper string with correct values
        res = self.first_worker.get_info()
        self.assertEqual('Worker_1 has saved 0 money.', res)


if __name__ == "__main__":
    main()
