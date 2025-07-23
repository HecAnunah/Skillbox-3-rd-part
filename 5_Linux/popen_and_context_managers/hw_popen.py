import subprocess
import shlex
import time


def run_programm():
    # commands = 'sleep 15 && echo "My mission is done here!"'
    commands = "sleep 4 && exit 1"
    start_time = time.time()
    process = []

    for i in range(1, 10):
        p = subprocess.Popen(
            commands, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True
        )
        process.append(p)
        print(f"Result use Popen process numb {i}: {p.pid}")

    for proc in process:
        try:
            # proc.wait(timeout=1)
            proc.wait()
            if proc.returncode == 1:
                print(proc)
                print("Process with PID {} ended successfully".format(proc.pid))
        except subprocess.TimeoutExpired as exc:
            print(f"Не прошли проверку if. Ошибка {exc}")

    print(f"Done in time {time.time() - start_time}")


if __name__ == "__main__":
    run_programm()
