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
There was no need for vote, there was only one valid submission by @angalaagl for:
https://github.com/aglpy/hangman

A Gif will follow. It was a well executed, multi language Hangman. Awesome!

It made use of the ASCII lib: https://github.com/sepandhaghighi/art
which allows you to write ASCII text in any ASCII font you like among others. Congratulations!
                '''.strip('\n').replace('\n', '<br>')
            },
        ],
        "call to action": "https://docs.google.com/forms/d/e/1FAIpQLSeamPyb_z-N_cjgGtFwOwlRgcbHD94nWVoZdyhF7ZUSKQc8PQ/viewform?usp=sf_link"
    },
    {
        "name": "Terminal Chat Tournament",
        "start": "Tue 20/April/2021",
        "end": "Sun 25/April/2021 midnight",
        "sections": [
            {
                "title": "Description",
                "info": '''
Build a terminal chat app using this code as base:
https://github.com/pymug/ARJ_SpoonfeedingSockets_APR2021/tree/main/04_chat
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
---
                '''.strip('\n').replace('\n', '<br>')
            },
        ],
        "call to action": "https://forms.gle/DGJ9WmjNFeN8k5fG6"
    }
]

info.update({
    'events': events
    })