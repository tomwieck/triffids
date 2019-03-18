
<p align="center"><a href="https://triffids.app" target="_blank" rel="noopener noreferrer"><img width="300" src="src/assets/logo-background.png" alt="Triffids Logo"></a></p>

### <strong>Triffids</strong> is an application that celebrates the parks, green spaces and nature of Bristol by surfacing data from Bristol Open Data and other sources in a fun and engaging way.

### https://triffids.app/

# Development Information

## API
- [API Endpoints](https://github.com/tomwieck/triffids/wiki/API-Endpoints)

- [Data Spec](https://github.com/tomwieck/triffids/wiki/Data-Spec)

- Relies heavily on the [Open Data Bristol](https://opendata.bristol.gov.uk/pages/homepage/) API
  - [Parks and Green Spaces](https://opendata.bristol.gov.uk/explore/dataset/parks-and-greens-spaces/information/)
  - [Trees](https://opendata.bristol.gov.uk/explore/dataset/trees/information/)


## Server setup
Virtualenv recommended - more information [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation)

```
mkvirtualenv triffids
workon triffids
pip3 install -r env/requirements.txt
```


```
cd server
python3 app.py
```

## Front end setup
> Ensure you are using Node version >=8
```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

## To deploy to firebase
`npm install -g firebase-tools` (if not already installed)

`firebase login` (Should only be required once)

`firebase deploy`

[More info](https://firebase.google.com/docs/hosting/deploying)

### Test deployment on Firebase
https://triffidsbcc.firebaseapp.com
