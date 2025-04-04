from telethon import TelegramClient
from config import config
import os
import importlib
import logging
import asyncio

logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

if config.get("api_id") == False and config.get("api_id") == False:
	apiid = input("enter api_id: ")
	apihash = input("enter api_hash: ")
	config.set("api_id", apiid)
	config.set("api_hash", apihash)
	config.save_config()

app = TelegramClient(
	'my_account',
	api_id=int(config.get("api_id")),
	api_hash=config.get("api_hash")
)

async def load_modules(client):
	modules_dir = 'modules'
	if not os.path.exists(modules_dir):
		logger.error(f"directory {modules_dir} not found!")
		return
	for filename in os.listdir(modules_dir):
		if filename.endswith('.py') and not filename.startswith('_'):
			module_name = filename[:-3]
			try:
				module = importlib.import_module(f'{modules_dir}.{module_name}')
				if hasattr(module, 'register'):
					await module.register(client)
					logger.info(f"module {module_name} loaded!")
			except Exception as e:
				logger.error(f"error with {module_name}: {e}")

async def main():
	await load_modules(app)
	await app.start()
	me = await app.get_me()
	app.owner_id = me.id
	await app.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
