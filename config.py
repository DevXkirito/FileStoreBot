import os

API_ID = int(os.environ.get("7391573", 0))
API_HASH = os.environ.get("1f20df54dfd91bcee05278d3b01da2c7", None)
BOT_TOKEN = os.environ.get("5285088021:AAGbxRFtj53in80VZXD4WmT2Ds0amMMqB8o", None)
DB_CHANNEL_ID = os.environ.get("-1002199830633")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID",'2092233990'))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001509463900')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
