from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

#config
id = 0
token = ""

#initialization bot
vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, id)

#get api methods
vk = vk_session.get_api()

#main loop
for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.message['text']:
		vk.messages.send(
			peer_id=event.message['peer_id'],
			message=event.message['text'],
			random_id=get_random_id()
		)
