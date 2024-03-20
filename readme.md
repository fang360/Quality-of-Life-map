This project is divided into two tasks:

I . The first task will translate the raw datasets into one for machine learning and analysis. To train the 
machine learning models, follow the below steps:
1. Run the transform.py file in “.\01_collect data\indicators cleaning”
> some part of data cleaning and preprocessing is done by QGIS (not code) 

2. Combine the dataset by running combine.py in “.\01_collect data\combine data”
3. Run Jupiter notebooks according to the file numbers 

II . The second task will use JavaScript to build a website. To build the website, follow the below instructions:
1. Create a Mapbox account and upload all zip files in the website folder.
2. Change the API and URL in all HTML files. 
3. Upload it to GitHub.
> Only do these steps when you want to create a new website. To open the existing website, please use this https://fang360.github.io/ link.

The sources of submitted code:
Code included or adapted from other sources:

⚫ Biplot: https://stackoverflow.com/questions/39216897/plot-pca-loadings-and-loading-in-biplotin-sklearn-like-rs-autoplot

⚫ Inertia: https://www.scikit-yb.org/en/latest/api/cluster

⚫ Radar plot: https://python-graph-gallery.com/390-basic-radar-chart/

⚫ Multi radar chart: https://python-graph-gallery.com/391-radar-chart-with-several-individuals/

⚫ History.html: 
- Sliderbar (html): https://docs.mapbox.com/mapbox-gl-js/example/timeline-animation/
- FlyTo function: Fly to a location | Mapbox GL JS | Mapbox
- Legend: Make a choropleth map, part 2: add interactivity | Help | Mapbox

⚫ Current.html:
- hr (css): http://monahousehold.blogspot.com/2017/05/hr.html
- Commuting time: https://docs.mapbox.com/help/tutorials/get-started-isochrone-api/
- Detail: Make a choropleth map, part 2: add interactivity | Help | Mapbox
- Search bar: Local search with the Geocoding API | Help | Mapbox

Used library:
Numpy, Pandas, Matplotlib, seaborn, sklearn, scipy, yellowbrick.
# Quality-of-Life-map
