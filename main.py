from fastapi import FastAPI
from typing import Union
import postgresql_connector as psql_conn
import fim_core


TL = fim_core.Task_List()
app = FastAPI()


@app.get("/info")
def info_message():
    return {"That's my info message"}


@app.get("/synchronization/")
def agent_synchronization(agent_id: int, agent_key: str, politics_key: str):

    actual_politics_key = fim_core.Politics.get_hash_politic()
    status = ""
    if agent_id == 0:
        status = "Invalid agent ID"
        return {"status": status}  # Добавить проверку наличия ID
    if agent_key == '':
        status = "Error of authentication agent"
        return {"status": status}  # Добавить сравнение ключа агента с его ID на актуальность
    actual_tasks = TL.check_tasks(agent_id)
    if politics_key != actual_politics_key:
        status = "Not actual politics"
        print("Actual politics: ", actual_politics_key)
        return {"status": status, "tasks": actual_tasks}
    status = "synchronized"
    return {"status": status, "tasks": actual_tasks}


@app.get("/upload_politic/")
def upload_politic_function(agent_id: int, agent_key: str):
    return {fim_core.Politics.get_politic()}


@app.post("/registration/")
def agent_registration(agent_id: int, agent_key: str, agent_name: str):

    agent = (agent_id, agent_key, agent_name)
    psql_conn.add_agent(agent)

    return {"status": "agent registrated"}



def main():
    a = 1


if __name__ == "__main__":
    main()
