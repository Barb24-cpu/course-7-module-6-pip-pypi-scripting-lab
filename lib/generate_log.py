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
   filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    # STEP 3: Write the log entries to a file using File I/O
   with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

  print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetches sample data from external API using requests."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
