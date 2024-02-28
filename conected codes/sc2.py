# import subprocess

# # output = subprocess.check_output(["C:\Program Files\Python312\python.exe", "A:\Python\MY_projects\opencv\conected codes\sc1.py"])
# output = subprocess.check_output(["C:\\Program Files\\Python312\\python.exe", "A:\\Python\\MY_projects\\opencv\\conected codes\\sc1.py"])


# print(output)

import subprocess
process = subprocess.Popen(["C:\\Program Files\\Python312\\python.exe", "A:\\Python\\MY_projects\\opencv\\conected codes\\sc1.py"], stdout=subprocess.PIPE)
while True:
    output = process.stdout.read(1)
    if output == b"" and process.poll() is not None:
        break
    if output:
        print(output.decode(), end="")
