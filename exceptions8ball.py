import requests # after installin in terminal fwith pip, import

question = input('Enter question for the magic 8 ball: ')

magic8ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    response = requests.get(magic8ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says: {answer}')
except Exception as e:
    print(e)
    print('Error connecting...')