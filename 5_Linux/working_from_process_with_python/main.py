import subprocess


def run_programm():
    result = subprocess.run(
        ["python3", "test_print.py"], stderr=subprocess.STDOUT, input=b'Someting string'
    )
    return result


if __name__ == "__main__":
    run_programm()
