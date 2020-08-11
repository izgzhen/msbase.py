# pip install PyMySQL path

import sys
import os

from msbase.utils import load_yaml
from msbase.mysql import DB

config_file = sys.argv[1]
config = load_yaml(config_file)["db"]

db = DB(os.path.dirname(config_file), config)
db.db_.close()

# Throw if not reconnected
# pymysql.err.InterfaceError: (0, '')
print(db.exec_fetch_one("SELECT * FROM users"))