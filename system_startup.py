#!/usr/bin/env python3
# """
# system_startup.py

# Simulates a simple system startup sequence using multiprocessing and logging.

# Generates a 'process_log.txt' file logging process start and end times.

# Usage:
#   python3 system_startup.py
# """

import multiprocessing
import time
import logging
import argparse
import os

LOGFILE = "process_log.txt"

def setup_logger():
    logging.basicConfig(
        filename=LOGFILE,
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def system_process(task_name, sleep_time=2):
    logging.info(f"{task_name} started")
    # simulate work
    time.sleep(sleep_time)
    logging.info(f"{task_name} ended")

def run_simulation(n_processes=2, sleep_time=2):
    setup_logger()
    print("System Starting...")
    processes = []
    for i in range(n_processes):
        p = multiprocessing.Process(target=system_process, args=(f"Process-{i+1}", sleep_time))
        processes.append(p)
        p.start()
        logging.info(f"Spawned {p.name} (PID {p.pid})")

    # Wait for all processes
    for p in processes:
        p.join()
        logging.info(f"{p.name} joined (PID {p.pid})")

    print("System Shutdown. Check process_log.txt for details.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate system startup with multiprocessing and logging")
    parser.add_argument("--n", type=int, default=2, help="Number of processes to spawn")
    parser.add_argument("--sleep", type=int, default=2, help="Seconds each process sleeps (simulates work)")
    args = parser.parse_args()
    run_simulation(args.n, args.sleep)
