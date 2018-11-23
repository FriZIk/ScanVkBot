# ScanTelegramBot
Port scanner executed on the server,driven through Telegram

## Work through Tor
If your provider blocks the connection with Telegram,use proxychains4.Commands to install and using:

```
sudo apt-get install torsocks tor
sudo apt-get install git gcc
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng/
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
proxychains4 python3 Main.py
```

## Settings in the code
You must provide your encryption key issued by botfather

```python
Key=("Enter key")
bot = telebot.TeleBot(Key)
```
