from vk_api import VkApi
from vk_api.utils import get_random_id 
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

id = 0
token = ""

vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, id)

vk = vk_session.get_api()

messages = {
	"message1":"Hello, world!",
	"message2":"Hi!",
}

def send_message_user(peer_id, text):
	vk.messages.send(
		message=text,
		peer_id=peer_id,
		random_id=get_random_id()
	)

def message_filter(message):
	for i in messages.items():
		if i[0] == message['text'].lower():
			send_message_user(message['peer_id'], i[1])
			return

	send_message_user(message['peer_id'], "Command not found")

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.message['text']:
		message_filter(event.message)
