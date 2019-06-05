cp ./colour-data-to-db.service /lib/systemd/system/colour-data-to-db.service &&
cp ./light-data-to-db.service /lib/systemd/system/light-data-to-db.service &&
cp ./motion-data-to-db.service /lib/systemd/system/motion-data-to-db.service &&
cp ./temperature-data-to-db.service /lib/systemd/system/temperature-data-to-db.service &&
sudo chmod 644 /lib/systemd/system/colour-data-to-db.service /lib/systemd/system/light-data-to-db.service /lib/systemd/system/motion-data-to-db.service /lib/systemd/system/temperature-data-to-db.service &&
sudo systemctl daemon-reload &&
sudo systemctl enable colour-data-to-db.service light-data-to-db.service motion-data-to-db.service temperature-data-to-db.service