# StellariumEphemerides
Display NASA Horizons Ephemerides data in Stellarium, based on nbhasker's [JWSTStellarium](https://github.com/nbhasker/JWSTStellarium) script. 

This set of scripts consumes NASA Horizons Ephemerides data for an object such as the JWST and allows it 
to be displayed in Stellarium.

## Using this script

First you will need some NASA Horizons data for the object you want to track.

To obtain the Horizons data go [here](https://ssd.jpl.nasa.gov/horizons/app.html), select the object, 
set your location and the desired time range, then click Generate Ephemerides and finally Download Results to 
save the file somewhere convenient on your computer. 

Now run the python script `convertHorizons.py`, supplying the full name to the file you downloaded. For example if you saved it in your downloads folder it might be: 

``` pwsh
python convertHorizons.py c:\users\yourname\downloads\jwst_horizons_data.txt
```
or, for Linux or MacOS with the file saved in /tmp:
``` bash
python convertHorizons.py /tmp/jwst_horizons_data.txt

```

This will create two files in the same folder as the python script, `jwst_horizons_data.inc` and `current_object.inc`

Now you can fire up Stellarium. Once it has loaded, press F12 to open the Script window. 
Click on the open-file icon at the top left of the dialog, and select `HorizonsToStellarium.ssc` from this folder. 

Run the script, and you should see some markers appear and Stellarium's viewpoint shift to the first marker. 

Thats it! 

Note that if you have a lot of data, Stellarium may take a while to process it (maybe 30 seconds). 

## Switching Objects
Each time you run the above process `current_object.inc` is overwritten with the latest data. If you want to switch back to a previous object, just copy its '.inc' file to `current_object.inc`. For example to switch back to the JWST data:

``` pwsh
copy jwst_horizons_data.inc current_object.inc
```

Then go into Stellarium and rerun the script. 

## What if the Object isn't in Horizons? 
If you have the RA and Dec of the object on a range of dates, you can manually update `current_object.inc` with the data. The file is pretty simple, it contains one variable that's the name of the object, and another that's an array containing some labels, RA and Dec values. 

You can put your own data in here, just be sure to use the same format. The RA must be in the format HH MM SS.nn  (hours, minutes, seconds with two decimals) and dec must be sDD MM SS.n (sign, degrees, minutes and seconds with one decimal). Single-digit values must have a leading zero as shown below.

```
var objname = "JWST";

var currentobject = [
        {label: "Jan 11", ra: "06 35 14.04", dec: "+01 59 09.1"},
        {label: "Jan 21", ra: "06 51 15.59", dec: "+04 09 18.7"},
        {label: "Jan 31", ra: "07 07 38.12", dec: "+06 54 19.5"},
        {label: "Feb 7",  ra: "07 22 31.41", dec: "+09 17 53.3"},
];

```