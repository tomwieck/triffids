# triffids

## Server setup

```
python app.py
```

## Project setup

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

### Run your tests

```
npm run test
```

### Lints and fixes files

```
npm run lint
```

### To deploy to firebase
`npm install -g firebase-tools` (if not already installed)
`firebase login` (Should be a one time login)
`firebase deploy`

[More info](https://firebase.google.com/docs/hosting/deploying)

### Test deployment on Firebase
https://triffidsbcc.firebaseapp.com


## Server setup
```
cd server
python app.py
```

Ensure Flask is installed - `pip install flask`
Virtualenv recommended - https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

## Available functions

```
getPark(parkCode)             - curl http://localhost:5000/server/park/"parkCode"
getAllParkNames()             - curl http://localhost:5000/server/allParkNames
getTrees(siteCode, lat, long) - curl http://localhost:5000/server/trees/"parkCode"/"lat"/"long"
getBenches(lat, long, radius) - curl http://localhost:5000/server/benches/"lat"/"long"/"radius"
```

For getTrees(siteCode, lat, long) pass 0s for lat and long to search by park site code. Pass coordinates to search by point instead

## Fields of interest

```
park:{
  "id":"FILWPA",
  "siteName":"Filwood Park",
  "lat":"51.4216453530745",
  "long":"-2.583616749058728",
  "geoShape":{
    "type":"Polygon",
    "coordinates":[
      [(too many elements to preview)]
    ]
  }
}

tree: {
  "prim_meas":"1",
  "dbh":"15 Centimetres",
  "site_name":"Connaught Primary School",
  "crown_area":"20.1 - 100 M2 (New)",
  "latin_code":"TIEU",
  "crown_height":"4",
  "dead":"N",
  "common_name":"Lime",
  "unit":"Number",
  "asset_id":"00088034",
  "site_code":"ED143933",
  "type":"Tree - BCC Other",
  "location_risk_zone":"Zone D - Low",
  "full_common_name":"Crimean lime",
  "plot_no":"100032",
  "latin_name":"Tilia x euchlora",
  "feat_gp":"TR",
  "geo_point_2d":[
    51.42787452983056,
    -2.586289143983529
  ],
  "crown_width":"6",
  "y":"170037.49",
  "x":"359335.42"
}
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

### To deploy to firebase

`npm install -g firebase-tools` (if not already installed)
`firebase login` (Should be a one time login)
`firebase deploy`

[More info](https://firebase.google.com/docs/hosting/deploying)

### Test deployment on Firebase

https://triffidsbcc.firebaseapp.com
