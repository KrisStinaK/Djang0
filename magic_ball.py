from random import choice


answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да',
           'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', '	Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Привет')

while True:
    print('Задайте мне вопрос и я вам отвечу')
    question = input()
    print(choice(answers))
    print('Хотите продолжить?')
    s = input()
    if s.lower() in ('yes', 'да'):
        continue
    else:
        break