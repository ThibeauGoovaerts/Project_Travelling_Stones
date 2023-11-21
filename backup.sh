sudo docker exec django python setMaintenance.py

sudo docker exec calloux-db pg_dump postgres -U postgres > backupPostgre

sudo docker commit -p django django-backup-snapshot
sudo docker commit -p nginx nginx-backup-snapshot
sudo docker commit -p caddy caddy-backup-snapshot

sudo docker save -o ../container-backup/django-backup-snapshot.tar django-backup-snapshot
sudo docker save -o ../container-backup/nginx-backup-snapshot.tar nginx-backup-snapshot
sudo docker save -o ../container-backup/caddy-backup-snapshot.tar caddy-backup-snapshot

sudo restic -r rclone:remote:backup-web backup --verbose ../container-backup/

sudo docker exec django python setMaintenance.py
