import json

class Config:
	def __init__(self, filename="config.json", default_config=None):
		self.filename = filename
		self.default_config = default_config or {}
		self.config = self.load_config()

	def load_config(self):
		try:
			with open(self.filename, "r") as f:
				config = json.load(f)
				self.default_config.update(config)
				return self.default_config 
		except FileNotFoundError:
			return self.default_config
		except json.JSONDecodeError:
			return self.default_config

	def save_config(self):
		with open(self.filename, "w") as f:
			json.dump(self.config, f, indent=4)

	def get(self, key, default=None):
		return self.config.get(key, default)

	def set(self, key, value):
		self.config[key] = value
		self.save_config()

default_config = {
	"api_id": False,
	"api_hash": False,
    "url": "https://i.pinimg.com/originals/78/e6/77/78e677384a1b99ad26af270b756dde17.gif"
}

config = Config(default_config=default_config)