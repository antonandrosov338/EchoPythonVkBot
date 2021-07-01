from vk_api import VkApi
from vk_api.utils import get_random_id 
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 

id = 164875377
token = "26085de8b445c57bf9808313b0475ee6b31324d1a6fc1de443ca8e6fa4e8c9df57348b5bcba38ef7c5279"

vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, id)

vk = vk_session.get_api()

messages = {
	"привет":"Привет, лошпед)))",
	"как дела?":"Да норм чел",
	"погнали выйдем":"Ты че баран, погнали раз на раз с братками",
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

	send_message_user(message['peer_id'], "Не понял чё сморозил")

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.message['text']:
		message_filter(event.message)
