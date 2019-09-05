# GeoData

Created SQLite Databases Only With The Most Main Nodes From OpenStreetMap Data.
The Main Nodes Are Nodes Wich Represent An Single Point With An Tag From The Following Types:

- aeroway *(Flughafen)*
- amenity *(Einrichtung)*
- craft *(Handwerk)*
- emergency *(Notfall)*
- leisure *(Freizeit)*
- man_made *(Von Menschen Erschaffene Bauliche Strukturen)*
- military *(Milit&auml;r)*
- place *(Ortsangaben)*
- power *(Energieversorgung)*
- shop *(Gesch&auml;fte)*
- vending *(Automaten)*

---

## Databases

I Tried To Keep The Databases Easy:
- No High Sophisticated Column Types
- No Foreign Keys
- No Indexes (Everyone Has Different Needs Anyway)
- No Triggers
- No Extensions

## Tables

### `META`

The Meta Table Stores Only The BoundingBox Of The Original `.osm` File:

*SQL:*

```sql
CREATE TABLE META (
    MINLAT DOUBLE NOT NULL, -- The Minimum Latitude
    MAXLAT DOUBLE NOT NULL, -- The Maximum Latitude
    MINLON DOUBLE NOT NULL, -- The Minimum Longitude
    MAXLON DOUBLE NOT NULL  -- The Maximum Longitude
);
```

*Example:*

|MINLAT|MAXLAT|MINLON|MAXLON|
|:----:|:----:|:----:|:----:|
|47,26543|55,14777|5,864417|15,05078|


### `NODE`

The Node Table Stores Only The Most Important Data From The Main Nodes:

*SQL:*

```sql
CREATE TABLE NODE (
    ID INTEGER NOT NULL PRIMARY KEY, -- An Simple Primarkey (The Node Id From OSM)
    LAT DOUBLE NOT NULL,             -- The Latitude
    LON DOUBLE NOT NULL,             -- The Longitude
    NAME TEXT,                       -- An Optional Name Of The Node (It's The Name In National Language)
    TAG TEXT NOT NULL,               -- The Tag Of The Node
    VALUE TEXT NOT NULL,             -- The Value From The Tag Of The Node
    VAR TEXT                         -- Variable Data (When The Node Is An Place, We Try To Get The Population)
);
```

*Example:*

|ID|LAT|LON|NAME|TAG|VALUE|VAR
|--|--:|--:|----|:-:|:---:|--:|
|289645|48,9475008|10,3844452|Nordhausen|place|village||
|359460|50,9155914|6,9412465|Papa-Pizza|amenity|fast_food||
|359829|50,9049155|6,9639535|Starcar Autovermietung|amenity|car_rental||
|359832|50,9051565|6,963755|Campus|amenity|restaurant|
|652134|50,1062969|8,7381202|Kaiserlei|place|locality||
|2455376|50,0031781|8,9908311|Mainhausen|amenity|parking||
|13675911|48,711173|9,4184961|Plochingen|place|town|13689|
|2746208|48,1331941|11,5762279|Reichenbachplatz|place|square||
|3325823|51,1130814|13,6571918|Grundm&uuml;hle|amenity|restaurant||
|5611431|49,3123946|12,7521772|Gschwand|place|village||
|8274226|49,8747471|8,660555|Toilette der Technischen Universit&auml;t Darmstadt|amenity|toilets||
|10192259|48,4060294|10,807393|Hammel|place|village||
|10467911|49,5562455|8,5333174|Rennschlag|amenity|parking||
|11201567|50,5640963|10,4145729|Steinwegkreuzung|place|locality||
|11595291|47,8755989|11,4666275|Gartenberg|place|suburb||
|12101531|49,6954443|8,6613432|Wilmshausen|place|village|680|
|12101533|49,6810158|8,6227577|Bensheim|place|town|39642|
|12231211|49,699932|8,7284773|Breitenwiesen|place|hamlet||
|13355228|48,7427584|9,3071685|Esslingen am Neckar|place|town|92261|
|14474402|53,4714406|9,8801135|Hausbruch|place|suburb|17009|

---

## ToDo

- Rename The Column `VAR` To `POPULATION (INT)`
- Add An Column `ELEVATION (INT)`
- Add An Column For The International Name


## Useful Links

- [OpenStreetMap Data Extracts](http://download.geofabrik.de)
- [OpenStreetMap Map Features](https://wiki.openstreetmap.org/wiki/DE:Map_Features)
