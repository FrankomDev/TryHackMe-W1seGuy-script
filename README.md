# [TryHackMe W1seGuy](https://tryhackme.com/room/w1seguy) Challenge Script
my easy script which can help you beat this level :>

## How to use it:
- ``git clone https://github.com/FrankomDev/TryHackMe-W1seGuy-script.git``
- ``cd TryHackMe-W1seGuy-script/``
- get first 8 digits of HEX <br>
![](https://github.com/FrankomDev/TryHackMe-W1seGuy-script/blob/main/img/image1.png)
- open ``bruteforce.py`` and put this 8 digits inside ``wanted`` variable
- run script ``python3 bruteforce.py`` (better do it outside VM)
- when key found copy it but without last character (for example if it was ``Q4apZ`` copy only ``Q4ap``)
- open ``check.py`` put last copied key inside ``key`` variable and full HEX inside ``hex_encoded`` variable
- run script ``python3 check.py``
- from list of strings get this one which looks like sentence and ends with ``}``, that's first flag :) <br>
![](https://github.com/FrankomDev/TryHackMe-W1seGuy-script/blob/main/img/image2.png)
- copy key and paste into connection with server and you get second flag
- Congrats! 
