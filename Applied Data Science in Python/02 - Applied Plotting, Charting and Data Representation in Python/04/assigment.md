# Log

## Montreal weather data

Cloud-to-ground lightning flashes in Montreal and Ann Arbor comparison over last ten years (2006-2016)

- README
ftp://ftp.tor.ec.gc.ca/Pub/Engineering_Climate_Dataset/Canadian_Weather_Energy_Engineering_Dataset_CWEEDS_2005/ZIPPED%20FILES/ENGLISH/CWEEDS%20documentation_Release9.txt
- Folder
  + 2016
    * ftp://ftp.tor.ec.gc.ca/Pub/Engineering_Climate_Dataset/Canadian_Weather_Energy_Engineering_Dataset_CWEEDS_2005/ZIPPED%20FILES/ENGLISH/
  + Historical
    * ftp://ftp.tor.ec.gc.ca/Pub/Engineering_Climate_Dataset/Canadian_Weather_Energy_Engineering_Dataset_CWEEDS_2005/ZIPPED%20FILES/ENGLISH/CWEEDS_v_Historical/

^\d{7}\w(\d{10}).{60}(\d).+$
$1,$2

https://www.ncdc.noaa.gov/data-access/severe-weather/lightning-products-and-services
ftp://ftp.ncdc.noaa.gov/pub/data/swdi/stormevents/

Montreal:
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.499,45.682",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.514,45.627",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.496,45.512",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.504,45.429",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.588,45.407",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.614,45.495",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.61,45.583",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.603,45.578",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.683,45.596",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.689,45.504",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.7,45.424",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.783,45.411",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.802,45.494",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.898,45.505",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.895,45.419",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-73.989,45.404",

Ann Arbor
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.736,42.293",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.712,42.231",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.782,42.226",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.806,42.3",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.621,42.4",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.609,42.311",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.603,42.217",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.603,42.121",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.719,42.118",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.808,42.131",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.925,42.122",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.916,42.199",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.897,42.299",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.911,42.391",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.769,42.405",
"https://www.ncdc.noaa.gov/swdiws/csv/nldn/19870101:20170101/?stat=tilesum:-83.703,42.415"


0.21(32 x 1) - 0.84(24.5) - 8.41(5.75) + 0.34(5.75 x 5.75) + 108.94

The NOAA data webservice proposes multiple services, one of them being the possibility to see the number of strikes per day per tile of 0.10 degree, since 1987.
To cover the all city of Montréal, 16 tiles are needed.
As Ann Arbor is smaller than Montréal, I took as many tiles as I need to arrive at the same amount than Montréal, by surrounding the city.

Datasets chosen cover those tiles, on a period from January 1st, 1987 to December 31st, 2016. I took the longest data range possible to have a more accurate response.

I wanted to know: How are thunderstorms in Ann Arbor different from those in Montréal, in quality terms?

This plot helps to answer to this question. Even if lightning is just a part of a storm (vertical and horizontal wind, rain, speed, power... being others) this is the aspect that interests me the most.

To represent the dataset, I chose a Kernel Density Estimation. We can see that
We can see on the graph that the highest probability of lightning flashes count is around 5 for Montréal, and around 8 for Ann Arbor. The graph is starting from 1, as we only consider storm days here.

Thus we can say that storms in Ann Arbor produces more lightnings than those happening in Montréal. This could let us think that storms are more powerful in Ann Arbor, but a deeper study would be required to confirm this hypothesis.
