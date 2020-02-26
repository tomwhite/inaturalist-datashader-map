# iNaturalist Datashader Map

A zoomable map of iNaturalist observations made using [Datashader](https://datashader.org/) and [Leaflet](https://leafletjs.com/).

<a href="https://storage.googleapis.com/inaturalist-datashader-map/index.html"><img src="inaturalist-observations.png" alt="iNaturalist observations"/></a>

More: [interactive map](https://storage.googleapis.com/inaturalist-datashader-map/index.html), [blog post](http://tom-e-white.com/datavision/09-inaturalist-observations.html).

## How to build the visualization

iNaturalist makes available a full dataset of observations, which is what I used to generate the map.

Go to https://www.inaturalist.org/pages/developers and look for the "GBIF DarwinCore Archive" link.
Download and unzip the archive, then move the _observations.csv_ to the _data_ directory.

Create a conda environment with the following (note that conda has a machine optimized version of datashader):

```bash
conda env create -f environment.yml
```

The preprocess the _observations.csv_ file to remove unneeded columns, and to convert the lat/long fields to metres.

```bash
python preprocess.py
```

Generate the tiles as follows:

```bash
python generate_tiles.py
```

Then run a webserver to serve them:

```
python -m http.server 8008
```

And open http://localhost:8008/
