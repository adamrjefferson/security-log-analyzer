import unittest
from log_analyzer import analyze

class LogAnalyzerTests(unittest.TestCase):
    def test_counts_failures_and_ignores_success(self):
        sample = ('Failed password for invalid user admin from 192.0.2.1 port 22 ssh2\n'
                  'Accepted password for alice from 192.0.2.1 port 22 ssh2\n'
                  'Failed password for root from 192.0.2.1 port 22 ssh2')
        self.assertEqual(analyze(sample)['192.0.2.1'], 2)

    def test_empty_log(self):
        self.assertEqual(dict(analyze('')), {})

if __name__ == '__main__':
    unittest.main()
