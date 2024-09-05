import psycopg2 as ps


def set_table_of_dirs(list_of_dirs):
    connection = ps.connect(host='localhost', user='postgres', password='postgres', database='FIM_DB', port='5432')
    cursor = connection.cursor()

    create_politics_tb = "CREATE TABLE IF NOT EXISTS FIM_POLITICS (fim_politic_id SERIAL PRIMARY KEY, directory VARCHAR(1024));"
    cursor.execute(create_politics_tb)
    connection.commit()

    delete_old_request = "DELETE FROM FIM_POLITICS"
    cursor.execute(delete_old_request)
    connection.commit()

    for directory in list_of_dirs:
        new_dir = directory
        add_dir_request = "INSERT INTO FIM_POLITICS VALUES (%s, %s);"
        cursor.execute(add_dir_request, new_dir)
        connection.commit()

    cursor.close()
    connection.close()


def get_table_of_dirs():
    connection = ps.connect(host='localhost', user='postgres', password='postgres', database='FIM_DB', port='5432')
    cursor = connection.cursor()

    create_politics_tb = "CREATE TABLE IF NOT EXISTS FIM_POLITICS (fim_politic_id SERIAL PRIMARY KEY, directory VARCHAR(1024));"
    cursor.execute(create_politics_tb)
    connection.commit()

    cursor.execute("SELECT * FROM FIM_POLITICS")
    connection.commit()

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result


def add_agent(agent):
    connection = ps.connect(host='localhost', user='postgres', password='postgres', database='FIM_DB', port='5432')
    cursor = connection.cursor()

    create_agent_tb = "CREATE TABLE IF NOT EXISTS AGENTS (agent_id SERIAL PRIMARY KEY, agent_key VARCHAR(1024), agent_name VARCHAR(1024));"
    cursor.execute(create_agent_tb)
    connection.commit()

    add_agent_request = "INSERT INTO AGENTS VALUES (%s, %s, %s);"
    cursor.execute(add_agent_request, agent)
    connection.commit()

    cursor.close()
    connection.close()
