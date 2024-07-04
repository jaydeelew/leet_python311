def process_log_file(log_file_path):
    with open(log_file_path, "r") as file:
        for line in file:
            # Process each line of the log file here
            yield line


# Use generator to process the log file
log_file_path = "/home/dan_wsl/leet_python311/logs.log"
log_generator = process_log_file(log_file_path)

for log_entry in log_generator:
    # perform actions on each log entry
    print(log_entry)
