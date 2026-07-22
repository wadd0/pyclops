sudo nano /etc/systemd/system/pyclops.service

sudo nano /home/rats/.env

sudo chmod 644 /etc/systemd/system/pyclops.service

sudo systemctl daemon-reload

sudo systemctl enable pyclops.service

sudo systemctl start pyclops.service