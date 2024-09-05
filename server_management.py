from fastapi import FastAPI
from typing import Union
import postgresql_connector as psql_conn
import fim_core


@app.get("/info")
def info_message():
    return {"That's my info message"}


def main():
    a = 1


if __name__ == "__main__":
    main()