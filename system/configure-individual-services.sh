cp ./{colour,light,motion,temperature}-data-to-db.service /lib/systemd/system/ && sudo chmod 644 /lib/systemd/system/{colour,light,motion,temperature}-data-to-db.service && sudo systemctl daemon-reload && sudo systemctl enable {colour,light,motion,temperature}-data-to-db.service