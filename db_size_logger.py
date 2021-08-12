import os
from datetime import datetime
import time

while os.path.exists('wish.db'):
    text = f"UTC: {datetime.utcnow()} - {os.stat('wish.db').st_size / 1024} Kb"
    print(text, file=open('db_size_log.txt', 'a'))
    time.sleep(600)