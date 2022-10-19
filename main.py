from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsm_anketa

admin.register_handlers_admin(dp)
client.register_handler_client(dp)
callback.register_handlers_callback(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)

extra.register_handlers_extra(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
