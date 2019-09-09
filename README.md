# GeoData

![World Top](./Images/worldtopo.png)

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

I Tried To Keep The Databases Very Easy:

- [X] No High Sophisticated Column Types
- [X] No Foreign Keys
- [X] No Indexes (Everyone Has Different Needs Anyway)
- [X] No Triggers
- [X] No Extensions Is Needed Or Used (For Example SpatiaLite)

Only Two Tables Are Created And Used. 

This Make The Database Very Easy To Use And Is An Advantage For Some Tools.

---

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

    NAME TEXT,                       -- The Name Of The Node (It's Mostly The Name In National Language)
    NAME_EN TEXT,                    -- The English Name Of The Node (When He Is Avaible)
    NAME_DE TEXT,                    -- The German Name Of The Node (When He Is Avaible)

    TAG TEXT NOT NULL,               -- The Tag Of The Node
    VALUE TEXT NOT NULL,             -- The Value From The Tag Of The Node

    POPULATION INTEGER,              -- The Population Of An City, Town Or Village
    ELEVATION INTEGER                -- The Elevation Of The Node (Meters Above Sea Level)
);
```

*Example:*

|ID|LAT|LON|NAME|NAME_EN|NAME_DE|TAG|VALUE|POPULATION|ELEVATION|
|-:|--:|--:|:---|:------|:------|:--|:----|---------:|--------:|
|21489671|-33,934444|18,869167|Stellenbosch|||place|town|60000||
|25470100|-33,9617051|25,6207519|Port Elizabeth|Port Elizabeth|Port Elizabeth|place|city|1050000||
|25503669|-25,7459374|28,1879444|Pretoria|Pretoria|Pretoria|place|city|741651|1339|
|124482342|-23,948502|31,137577|Phalaborwa|||place|town|13108|436|
|259130371|-30,6527617|27,926089|Ice Station 2720|||amenity|pub||2720|
|262705211|-25,418349|30,104624|Dullstroom|||place|village|558|2100|
|25928779|-34,051111|24,922222|Jeffreys Bay|||place|town|27107||
|26417322|-26,1563889|27,8858333|Roodepoort|||place|city|325000||


---

## Useful Links

- [OpenStreetMap Data Extracts](http://download.geofabrik.de)
- [OpenStreetMap Map Features](https://wiki.openstreetmap.org/wiki/DE:Map_Features)
