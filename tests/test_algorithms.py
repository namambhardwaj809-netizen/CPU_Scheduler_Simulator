import unittest
from algorithms import fcfs, sjf, priority_scheduling, round_robin


class TestSchedulingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.processes = [
            {"pid": "P1", "arrival": 3, "burst": 4, "priority": 2},
            {"pid": "P2", "arrival": 0, "burst": 2, "priority": 1},
            {"pid": "P3", "arrival": 1, "burst": 3, "priority": 3}
        ]

    def check_results(self, results, expected):
        actual = {p["pid"]: p for p in results}

        for pid, values in expected.items():
            for field, value in values.items():
                self.assertEqual(actual[pid][field], value)

    def test_fcfs(self):
        results = fcfs(self.processes)
        self.check_results(results, {
            "P1": {"start": 5, "completion": 9, "waiting": 2},
            "P2": {"start": 0, "completion": 2, "waiting": 0},
            "P3": {"start": 2, "completion": 5, "waiting": 1}
        })

    def test_sjf(self):
        results = sjf(self.processes)
        self.check_results(results, {
            "P1": {"start": 5, "completion": 9},
            "P2": {"start": 0, "completion": 2},
            "P3": {"start": 2, "completion": 5}
        })

    def test_priority(self):
        results = priority_scheduling(self.processes)
        self.check_results(results, {
            "P1": {"start": 5, "completion": 9},
            "P2": {"start": 0, "completion": 2},
            "P3": {"start": 2, "completion": 5}
        })

    def test_round_robin(self):
        results, gantt = round_robin(self.processes, 2)
        self.check_results(results, {
            "P1": {"completion": 9, "waiting": 2, "turnaround": 6},
            "P2": {"completion": 2, "waiting": 0, "turnaround": 2},
            "P3": {"completion": 7, "waiting": 3, "turnaround": 6}
        })
    def test_process_arriving_after_cpu_idle_time(self):
        process = [
            {"pid": "P1", "arrival": 5, "burst": 2, "priority": 1}
        ]

        for algorithm in (fcfs, sjf, priority_scheduling):
            with self.subTest(algorithm=algorithm.__name__):
                result = algorithm(process)[0]
                self.assertEqual(result["start"], 5)
                self.assertEqual(result["completion"], 7)
                self.assertEqual(result["waiting"], 0)
                self.assertEqual(result["turnaround"], 2)
                self.assertEqual(result["response"], 0)


if __name__ == "__main__":
    unittest.main()
