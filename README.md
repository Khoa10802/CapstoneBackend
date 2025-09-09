# _Installation_
## 1. Update System
``` bash
sudo apt update & sudo apt upgrade -y
```

## 2. Clone the Repository
``` bash
git clone https://github.com/Khoa10802/CapstoneBackend
cd CapstoneBackend
```

## 3. Create Virtual Environment
- Create virtual environment
``` bash
python3 -m venv .venv
```
If prompted to download `python3-env`, go for it.

- Activate virtual environment
``` bash
. .venv/bin/activate
```

- Install required packages
``` bash
pip install -r requirements.txt
```

## 4. Install Gunicorn & nginx
- Install `nginx`
``` bash
sudo apt install nginx -y
```

- Install `gunicorn`
``` bash
pip install gunicorn
```
## 5. Edit Gunicorn Config File
- Create config file
``` bash
sudo nano /etc/systemd/system/flask-app.service
```

- Edit config file
```
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/CapstoneBackend
Environment="PATH=/home/ubuntu/CapstoneBackend/.venv/bin"
ExecStart=/home/ubuntu/CapstoneBackend/.venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```
## 6. Start and Enable Flask Service
``` bash
sudo systemctl daemon-reload
sudo systemctl start flask-app
sudo systemctl enable flask-app
```

``` bash
# Check status
sudo systemctl status flask-app
```

## 7. Configurate Firewall
- Enable & Allow port 5000
``` bash
sudo ufw enable
sudo ufw allow 5000
```

``` bash
# Check firewall status 
sudo ufw status
```
## 8. Restart nginx
``` bash
sudo systemctl restart nginx
```

# _Troubleshooting_
