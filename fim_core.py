import hashlib
import postgresql_connector as psql_conn


class Task_List:


    def __init__(self):
        self.tasklist = []
        self.searchable_agent_id = 0

    def add_task(self, num_of_task: int, agents_list: set):
        self.tasklist.append((num_of_task, agents_list))

    def check_one_task(self, agent_id, element):
        num = agent_id in element[1]
        element[1].discard(agent_id)
        return num

    def check_tasks(self, agent_id):
        tasks_nums_for_agent = list()
        for element in self.tasklist:
            if self.check_one_task(agent_id, element):
                tasks_nums_for_agent.append(element[0])
        return tasks_nums_for_agent


class Politics:

    @staticmethod
    def get_politic():
        table_of_dirs = psql_conn.get_table_of_dirs()
        politic_str = ""
        for politic in table_of_dirs:
            politic_str = politic_str + ' ' + politic[1]
        return politic_str
    @staticmethod
    def get_hash_politic():
        table_of_dirs = psql_conn.get_table_of_dirs()
        politic_str = ""
        for politic in table_of_dirs:
            politic_str = politic_str + politic[1]
        hash_object = hashlib.sha256(politic_str.encode('utf-8'))

        return hash_object.hexdigest()


if __name__ == "__main__":
    print(Politics.get_hash_politic())
