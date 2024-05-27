import os

# TOKENS
BOT_TOKEN = os.getenv("BOT_TOKEN")


DB_API_URL = os.getenv("DB_API_URL")
DB_API_AUTH_TOKEN = os.getenv("DB_API_AUTH_TOKEN")

# Other variables
MODEL_TO_USE_PATH = "models/efficient_net_b1.onnx"


CLASS_MAPPING = {
  '10010': 0,
  '10011': 1,
  '10024': 2,
  '10050': 3,
  '10053': 4,
  '10031': 5,
  '10067': 6,
  '10068': 7,
  '10003': 8,
  '10004': 9,
  '10013': 10,
  '10014': 11,
  '10015': 12,
  '10016': 13,
  '10017': 14,
  '10018': 15,
  '10023': 16,
  '10046': 17,
  '10047': 18,
  '10001': 19,
  '10002': 20,
  '10005': 21,
  '10006': 22,
  '10008': 23,
  '10019': 24,
  '10020': 25,
  '10039': 26,
  '10041': 27,
  '10077': 28,
  '10091': 29,
  '10092': 30,
  '10104': 31,
  '10105': 32
}

REVERSE_CLASS_MAPPING = {v: k for k, v in CLASS_MAPPING.items()}

# threshold for sneakers existence on photo
SNEAKERS_THRESHOLD = float(os.getenv("SNEAKERS_THRESHOLD"))
