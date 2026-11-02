# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from datetime import datetime
import unittest
from alarmPiano import seconds_until_alarm

class AlarmTests(unittest.TestCase):
    def test_same_day(self):
        now = datetime(2026, 11, 2, 8, 0)
        self.assertEqual(seconds_until_alarm("08:30", now), 1800)
    def test_next_day(self):
        now = datetime(2026, 11, 2, 9, 0)
        self.assertEqual(seconds_until_alarm("08:30", now), 23.5 * 3600)
    def test_invalid(self):
        for value in ("25:00", "12:60", "bad", "9:30"):
            with self.assertRaises(ValueError):
                seconds_until_alarm(value, datetime(2026, 11, 2))

if __name__ == "__main__":
    unittest.main()
