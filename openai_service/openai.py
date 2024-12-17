import openai

from config.values import OPEN_AI_API_KEY

client = openai.OpenAI(api_key=OPEN_AI_API_KEY)

def get_text_chat(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'Расскажи мне о достопримечательности в Москве под названием {prompt}'
            }
        ],
        model='gpt-4o'
    )
    return response

def get_location_chat(latitude:float, longitude: float):
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'''Расскажи мне о локальных достопримечательностях рядом с этими 
                координатами {latitude}, {longitude} и укажи расстояние до каждого из них. 
                Если место с этими координатами находится не в Москве верни сообщение строго "Укажите место в Москве."
                Преимущественно смотри на объекты на сайте: https://stapelia2784.livejournal.com/60420.html
                В конце ответа гиперссылкой оформи вышеуказанный ресурс
                В тексте ответа не используй полученные координаты'''
            }
        ],
        model='gpt-4o'
    )
    return response