# Server

## Setup

```
$ virtualenv --python=3.6 venv # for example
$ pip3 install -r env/requirements.txt
$ source venv/bin/activate
## do yer stuff
$ deactivate
```

## Live server setup

- On Ubuntu 16.04
- Install Python, Node, uWSGI, NginX
- run the Python server with `sudo systemctl start triffidsapi`
- check status/logs with `sudo systemctl status triffidsapi`


## Testing

Requires `pytest`

`cd server`
`$ pytest`

