# Piano Alarm Clock

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A modern Python 3/Tkinter local alarm clock. The alarm accepts a 24-hour HH:MM time, schedules the next occurrence, and uses the desktop bell plus a message. It replaces the EasyGUI busy-wait loop and does **not automatically open YouTube links or external websites**.

```sh
python3 alarmPiano.py
python3 -m unittest discover -s tests -v
```

Keep the application running for the alarm to fire. Computer sleep, muted desktop bells and daylight-saving changes may affect reliability. This is not a critical alert system. Original version: [old branch](https://github.com/hamdyaea/Piano-Alarm-Clock/tree/old).
