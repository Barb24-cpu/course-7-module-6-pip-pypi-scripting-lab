from datetime import datetime
import os

def generate_log(data):
    """Generates a log file with timestamped name containing log entries.

    Raises ValueError if input is not a list.
    """
    # STEP 1: Validate input
   if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    pass
