import os
import csv
from datetime import datetime


def long_chat(session_id:str,query:str,response:str,is_crisis:bool):
    long_file = "chat_log.csv"
    file_exist = os.path.isfile(long_file)

    with open(long_file,mode='a',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exist:
            writer.writerow(["timestamp","session_id","query","response","crisis_flag"])
        writer.writerow([
            datetime.now().isoformat(),
            session_id,
            query,
            response,
            str(is_crisis)
        ])