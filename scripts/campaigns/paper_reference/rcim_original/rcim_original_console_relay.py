"""Relay RCIM original training stages to console and log files.

This wrapper keeps the child training command attached to the active console
while duplicating stdout and stderr into persistent log files.
"""

from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import threading
from pathlib import Path


TRAINING_SCRIPT_PATH = (
    "scripts/paper_reimplementation/rcim_ml_compensation/"
    "recovered_original_workflow/training_models.py"
)


def parse_arguments() -> argparse.Namespace:

    """ Parse Relay Arguments. """

    parser = argparse.ArgumentParser(description="Mirror RCIM original training stage output to console and logs.")
    parser.add_argument("--working-directory", required=True)
    parser.add_argument("--stdout-log-path", required=True)
    parser.add_argument("--stderr-log-path", required=True)
    parser.add_argument("--combined-log-path", required=True)
    parser.add_argument("training_arguments", nargs=argparse.REMAINDER, help="Training-model arguments prefixed by '--'.")
    return parser.parse_args()

def normalize_training_argument_list(argument_list: list[str]) -> list[str]:

    """ Drop the Argparse Remainder Separator when Present. """

    # Training Arguments Expected to After a "--" Separator
    if argument_list and argument_list[0] == "--": return argument_list[1:]
    return argument_list

def stream_pipe_to_console_and_logs(
    stream,
    console_stream,
    stage_log_handle,
    combined_log_handle,
    combined_log_lock: threading.Lock,
) -> None:

    """ Forward One Child Stream to Console and Persistent Logs. """

    try:
        for line in iter(stream.readline, ""):
            if not line: break
            console_stream.write(line)
            console_stream.flush()
            stage_log_handle.write(line)
            stage_log_handle.flush()
            with combined_log_lock:
                combined_log_handle.write(line)
                combined_log_handle.flush()
    finally:
        stream.close()

def send_interrupt_to_child_process(child_process: subprocess.Popen[str]) -> None:

    """ Ask the Child Process to Stop as Cleanly as Possible. """

    if os.name == "nt":

        # Ctrl-Break on Windows
        try: child_process.send_signal(signal.CTRL_BREAK_EVENT); return
        except Exception: pass

    # SIGINT on Unix
    try: child_process.send_signal(signal.SIGINT)
    except Exception:

        # SIGKILL on Unix
        try: child_process.terminate()
        except Exception: pass

def main() -> int:

    """ Run the Relay. """

    # Parse Arguments
    arguments = parse_arguments()
    training_argument_list = normalize_training_argument_list(arguments.training_arguments)

    # Prepare Child Command
    child_command = [
        sys.executable,
        "-u",
        "-B",
        TRAINING_SCRIPT_PATH,
        *training_argument_list,
    ]

    # Prepare Child Process
    working_directory = Path(arguments.working_directory)
    stdout_log_path = Path(arguments.stdout_log_path)
    stderr_log_path = Path(arguments.stderr_log_path)
    combined_log_path = Path(arguments.combined_log_path)

    # Prepare Log Directories
    stdout_log_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_log_path.parent.mkdir(parents=True, exist_ok=True)
    combined_log_path.parent.mkdir(parents=True, exist_ok=True)

    # Create Child Process
    creationflags = 0
    if os.name == "nt": creationflags = subprocess.CREATE_NEW_PROCESS_GROUP

    with (
        stdout_log_path.open("a", encoding="utf-8", newline="") as stdout_log_handle,
        stderr_log_path.open("a", encoding="utf-8", newline="") as stderr_log_handle,
        combined_log_path.open("a", encoding="utf-8", newline="") as combined_log_handle
    ):

        # Run Child Process with Output Piped for Relay
        combined_log_lock = threading.Lock()
        child_process = subprocess.Popen(
            child_command,
            cwd=str(working_directory),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
            universal_newlines=True,
            creationflags=creationflags,
        )

        # Relay Child Process Output
        stdout_thread = threading.Thread(
            target=stream_pipe_to_console_and_logs,
            args=(
                child_process.stdout,
                sys.stdout,
                stdout_log_handle,
                combined_log_handle,
                combined_log_lock,
            ),
            daemon=True,
        )

        # Relay Child Process Errors
        stderr_thread = threading.Thread(
            target=stream_pipe_to_console_and_logs,
            args=(
                child_process.stderr,
                sys.stderr,
                stderr_log_handle,
                combined_log_handle,
                combined_log_lock,
            ),
            daemon=True,
        )

        # Relay Child Process Output
        stdout_thread.start()
        stderr_thread.start()
        interrupted = False

        # Wait for Child Process to Finish
        try: return_code = child_process.wait()
        except KeyboardInterrupt:

            # Forward Ctrl+C to Child Process
            interrupted = True
            sys.stderr.write("[WARNING] KeyboardInterrupt received. Forwarding stop signal to child process.\n")
            sys.stderr.flush()
            send_interrupt_to_child_process(child_process)

            # Wait for Child Process to Finish
            try: return_code = child_process.wait(timeout=10)
            except subprocess.TimeoutExpired:

                # Forcefully Terminate Child Process
                sys.stderr.write("[WARNING] Child process did not stop after interrupt. Terminating forcefully.\n")
                sys.stderr.flush()
                child_process.kill()
                return_code = child_process.wait()

        # Join Relay Threads
        stdout_thread.join()
        stderr_thread.join()

    # Return Exit Code
    if interrupted and return_code == 0: return 130
    return return_code

if __name__ == "__main__":

    raise SystemExit(main())
