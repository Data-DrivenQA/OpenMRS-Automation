import subprocess
import sys

def run_test_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{script_name} succeeded.")
    else:
        print(f"{script_name} failed.")
        print("Output:\n", result.stdout)
        print("Error:\n", result.stderr)

if __name__ == "__main__":
    test_scripts = [
        "login_test.py",
        "successfullogin_test.py",
        "errorhandling_test.py"
    ]

    for script in test_scripts:
        run_test_script(script)
