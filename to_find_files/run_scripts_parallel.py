# Executes all Python scripts in the current and subdirectories in parallel using available CPU cores, 
# logging any script failures to a specified error log file.
import os
import subprocess
from multiprocessing import Pool, cpu_count

# Define the log file for errors
error_log_file = "error_log.txt"

# Clear the log file at the start
with open(error_log_file, "w") as log_file:
    log_file.write("")


def run_script(script_path):
    """
    Function to run a Python script and log errors if it fails.
    """
    try:
        subprocess.run(
            ["python3", script_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return None  # No error
    except subprocess.CalledProcessError:
        return script_path  # Return the script path if it failed


def get_all_python_scripts(root_dir, exclude_script):
    """
    Get a list of all Python scripts in the directory and subdirectories,
    excluding the current script.
    """
    scripts = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py") and os.path.abspath(os.path.join(subdir, file)) != exclude_script:
                scripts.append(os.path.join(subdir, file))
    return scripts


def main():
    # Get the absolute path of the current script to avoid executing it
    current_script = os.path.abspath(__file__)

    # Get all Python scripts, excluding the current script
    scripts = get_all_python_scripts(os.getcwd(), current_script)

    # Get the number of available processors
    num_cores = cpu_count()

    # Use a multiprocessing Pool to run scripts in parallel
    with Pool(num_cores) as pool:
        results = pool.map(run_script, scripts)

    # Log errors
    with open(error_log_file, "a") as log_file:
        for script in results:
            if script:  # If the script failed
                log_file.write(f"Error in script: {script}\n")


if __name__ == "__main__":
    main()
