import json

OUTPUT_FOLDER = 'docs/'
info = None

with open('info.json') as f:
    info = json.load(f)

events = [
    {
        "name": "Hangman Tournament",
        "start": "Mon 12/April/2021",
        "end": "Thur 15/April/2021",
        "sections": [
            {
                "title": "Description",
                "info": '''
Build a commandline hangman with Python.
Use your creativity. No copy pasting.
Let's see what's the best we can get.
                '''.strip('\n').replace('\n', '<br>')
            },
            {
                "title": "Winning",
                "info": '''
All submissions will be subjected to vote on the channel.
Winner will be put under this block with all his social media links.
                '''.strip('\n').replace('\n', '<br>')
            },
            {
                "title": "Winner/s",
                "info": '''
...
                '''.strip('\n').replace('\n', '<br>')
            },
        ],
        "call to action": "https://docs.google.com/forms/d/e/1FAIpQLSeamPyb_z-N_cjgGtFwOwlRgcbHD94nWVoZdyhF7ZUSKQc8PQ/viewform?usp=sf_link"
    }
]

info.update({
    'events': events
    })