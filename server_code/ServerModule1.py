import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import psycopg2
from datetime import datetime

@anvil.server.callable
def say_hello(name, photo):
    print(f"Hello, {name}")
    app_tables.visitors.add_row(name=name, when=datetime.now(), picture=photo)
