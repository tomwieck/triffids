# triffids

## FE setup
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
python -m pico.server example
```

Ensure pico is installed - `pip install pico`
Virtualenv recommended - https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

## Available functions
```
getPark(name)                 - curl http://localhost:4242/server/getPark/?name="Filwood Park"
getAllParkNames()             - curl http://localhost:4242/server/getAllParkNames"
getTrees(siteCode, lat, long) - curl http://localhost:4242/server/getTrees/?siteCode="FILWPA"&lat=0&long=0
getBenches(lat, long, radius) - curl http://localhost:4242/server/getBenches/?lat=0&long=0&radius=0
```

For getTrees(siteCode, lat, long) pass 0s for lat and long to search by park site code. Pass coordinates to search by point instead

## Fields of interest

```
park:{
  "site_name":"Filwood Park",
  "objectid":"4107",
  "site_code":"FILWPA",
  "geo_point_2d":[
      51.4216453530745,
      -2.583616749058728
  ],
  "uprn":"000000303842",
  "geo_shape":{
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



