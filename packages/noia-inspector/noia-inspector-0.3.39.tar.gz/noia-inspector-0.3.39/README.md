# NOIA Inspector

This README documents whatever steps are necessary to get NOIA Inspector up and running.

`python3`

`linux only`

`You must run as root and have wireguard installed` 

Install NOIA Inspector as `root` user

```
pip3 install noia-inspector
```

Run CLI Api, connect to SDN

```
noia-inspector --help
```
Connect to any host you want
```
noia-inspector
```

Run SDN tests using predefined speedtest server list in /etc/noia-inspector/destinations.json

```
noia-inspector-test
```

Run Inspector Api

```
noia-api
```

# How to use

For the first time , execute `noia-inspector` or `noia-inspector-test` and you will be prompted with initial configuration.


You will have to enter: 

- Email

- JWT token

- Wireguard public key location e.g. `/etc/wireguard/publickey`

- Wireguard private key location e.g. `/etc/wireguard/privatekey`

Settings locations:
```
/etc/noia-inspector/default.env
/etc/noia-inspector/destinations.json
```