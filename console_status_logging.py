# Have you seen those cool console apps that show a status in the console without adding new lines?
# You could do something similar with the following code
import time

current_status = ""

def log_message(message):
    global current_status
    # First we delete the current status
    # Special character to remove the whole line
    # http://wiki.lihebi.com/ascii.html
    print(f"\33[2K\r{message}")
    # After the message we add the current status
    print(current_status, end="", flush=True)

def log_status(status):
    global current_status
    current_status = status
    print(f"\33[2K\r{status}", end="")

files_count = 0
while True:
    files_count +=1
    log_status(f"Downloaded {files_count} files")
    if files_count % 10 == 0:
        log_message("Nice message!")
    time.sleep(0.5)