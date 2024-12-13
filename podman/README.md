
### Local Unifi Network App in container images
- Definition in file: `compose-unifi-network-app.yaml`
- command: `podman-compose -f compose-unifi-network-app.yaml up -d`
- Url to app: https://localhost:8080
- Update firewall settings to detect Ubiquity devices on local network
```
sudo firewall-cmd --zone=public --add-port=3478/udp --permanent
sudo firewall-cmd --zone=public --add-port=10001/udp --permanent
sudo firewall-cmd --zone=public --add-port=8443/tcp --permanent
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
```
