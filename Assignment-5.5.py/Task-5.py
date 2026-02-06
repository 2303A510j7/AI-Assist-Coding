#task5
#Generate a Python script that logs user activity including username, IP address, and timestamp.
import logging
from datetime import datetime
logging.basicConfig(filename='user_activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')
def log_user_activity(username, ip_address):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f'Username: {username}, IP Address: {ip_address}, Timestamp: {timestamp}')
username = input("Enter your username: ")
ip_address = input("Enter your IP address: ")
log_user_activity(username, ip_address)
print("User activity logged successfully.")