# NetRecon

NetRecon est un outil de reconnaissance réseau tout-en-un écrit en Python.

## Fonctionnalités

- Scan de ports TCP
- Sniffer de paquets réseau (avec Scapy)
- Lookup IP vers pays (GeoIP)
- Recherche WHOIS

## Utilisation

```

py netrecon.py scan --ip 192.168.1.1 --ports 20-1000
py netrecon.py sniff --iface eth0
py netrecon.py geoip --ip 8.8.8.8
py netrecon.py whois --target google.com

```

## Dépendances

Installez-les avec :

```

pip install -r requirements.txt

```

## Auteurs

Projet éducatif et open-source. Utilisation responsable uniquement.