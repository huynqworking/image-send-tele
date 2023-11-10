import os
from subprocess import check_output

dir_list = os.listdir()
for fi in dir_list:
    if ".jpg" in fi \
        or ".png" in fi \
        or ".svg" in fi:
        check_output('curl -v -F "chat_id=-4040713227" -F document=@./{}  https://api.telegram.org/bot5760836886:AAEwSLqQtsaDI32MjZXwNlf9fan7CB16fPs/sendDocument'.format(fi), shell=True).decode()

print("OK")
