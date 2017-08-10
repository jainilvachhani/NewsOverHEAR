Created during IEEE Impuslse 2017 Hackathon. Won 1st prize.

Title : NewsOverHEAR

Idea Abstract : News OverHEAR is powerfully scrapping the web to convey news progressively. We also categorised the news for faster access. It has features like voice search for processing questions faster, Play/Stop button to build client collaboration, Email based membership to hold clients, Manual searching if there is any occurrence of inaccessibility of microphone due to noise.

Technology Stack
- HTML5
- CSS3
- JavaScript
- Python

FrameWork : Django

API: 
- ResponsiveVoice.js 
- Aanyang 
- BeautifulSoap.py

How to run:
Create 'overhear' named database on your mysql server

set you mysql server's credentials in settings.py file

open terminal at project's main folder where manage.py file exist

make migrations of the database using following command
>python manage.py makemigrations 

migrate it to your server using,
>python manage.py migrate

now start Django server
>python manage.py runserver

In browser, type following IP 
>127.0.0.1:8000/hear1/index
