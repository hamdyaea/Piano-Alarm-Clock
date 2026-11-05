#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Local Tkinter alarm clock without busy-wait or automatic web browsing."""
from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

def seconds_until_alarm(value: str, now: datetime | None = None) -> float:
    now = now or datetime.now()
    try:
        hour, minute = map(int, value.split(":"))
    except (ValueError, AttributeError) as exc:
        raise ValueError("Time must be HH:MM") from exc
    if not (0 <= hour <= 23 and 0 <= minute <= 59) or len(value) != 5:
        raise ValueError("Time must be HH:MM in 24-hour format")
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return (target - now).total_seconds()

def main() -> None:
    root = tk.Tk()
    root.title("Piano Alarm Clock")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    time_var = tk.StringVar(value="08:30")
    status = tk.StringVar(value="Set a local alarm")
    target = None
    artwork = tk.PhotoImage(file=str(Path(__file__).resolve().parent / "images/piano-ui.png"))
    illustration = tk.Label(frame, image=artwork)
    illustration.image = artwork
    illustration.pack()
    ttk.Label(frame, text="Alarm time (HH:MM, 24-hour)").pack(pady=8)
    ttk.Entry(frame, textvariable=time_var, width=12).pack()
    ttk.Label(frame, textvariable=status).pack(pady=12)
    def ring() -> None:
        nonlocal target
        if target is None:
            return
        if datetime.now() >= target:
            target = None
            root.bell()
            messagebox.showinfo("Alarm", "It's time!", parent=root)
            status.set("Alarm finished")
        else:
            root.after(500, ring)
    def set_alarm() -> None:
        nonlocal target
        try:
            delay = seconds_until_alarm(time_var.get())
        except ValueError as exc:
            messagebox.showerror("Invalid time", str(exc), parent=root)
            return
        target = datetime.now() + timedelta(seconds=delay)
        status.set(f"Alarm set for {target:%Y-%m-%d %H:%M}")
        root.after(500, ring)
    def cancel() -> None:
        nonlocal target
        target = None
        status.set("Alarm cancelled")
    ttk.Button(frame, text="Set alarm", command=set_alarm).pack(side="left", padx=30)
    ttk.Button(frame, text="Cancel", command=cancel).pack(side="right", padx=30)
    root.mainloop()

if __name__ == "__main__":
    main()
