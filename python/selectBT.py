import subprocess

sinks = subprocess.run(["pacmd", "list-sinks"], capture_output=True).stdout
print(sinks.length)


