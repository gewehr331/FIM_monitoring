import threading
import time
import requests
import json

agent_configuration = open('agent_configuration.conf', 'r')
server_ip = ""
server_port = ""
agent_id = ""
politics_key = ""
agent_key = ""
for conf_str in agent_configuration:
    if conf_str.startswith("server_ip"):
        server_ip = conf_str[10:-1]
    elif conf_str.startswith("server_port"):
        server_port = conf_str[12:-1]
    elif conf_str.startswith("agent_id"):
        agent_id = conf_str[9:-1]
    elif conf_str.startswith("politics_key"):
        politics_key = conf_str[13:-1]
    elif conf_str.startswith("agent_key"):
        agent_key = conf_str[10:-1]


def synchronization():
    session = requests.Session()

    sync_result = session.get(f"http://{server_ip}:{server_port}/synchronization/?agent_id={agent_id}&agent_key={agent_key}&politics_key={politics_key}").text
    sync_result_data = json.loads(sync_result)

    if sync_result_data["status"]=="Not actual politics":
        update_result = session.get(f"http://{server_ip}:{server_port}/upload_politic/?agent_id={agent_id}&agent_key={agent_key}").text
        print(update_result)


if __name__ == "__main__":
    synchronized_thread = threading.Thread(target=synchronization)
    synchronized_thread.start()
    synchronized_thread.join()
