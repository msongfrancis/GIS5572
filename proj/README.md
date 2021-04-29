# Final Project: Using Fuzzy Suitability Analysis to Find Potential Retail Locaitons for Costco in the Metropolitan Counties in Minnesota

Maisong Francis
leex6165@umn.edu

The goals of this lab were to utilized demographic data and proximity data in a fuzzy suitability analysis to determine the most suitabile census tracts for a potential Costco Location

### License
Requires the ArcGIS Pro Spatial Analyst license

### Files
* Final Project Prospectus.docx
    * Format: docx
    * Description: Intial report for project idea. 

* Final_Project_Report.docx
    * Format: docx
    * Description: Report writeup for final project and results. 

* /output_data/competing.csv
    * Format: csv
    * Description: location of competing businesses retrieved from google places API 

* /output_data/costco_loc.csv
    * Format: csv
    * Description: location of existing costcos retrieved from google places API 

* /output_data/demographics.csv
    * Format: csv
    * Description: concatenation of demographics data used in the analysis. Obtained from the US census and ACS surveys.

* /results/FuzzyOverlay_Results.jpg
    * Format: jpeg
    * Description: results from fuzzy overlay with planned land use considered. 

* /results/FuzzyOverlay_Results_noLU.jpg
    * Format: jpeg
    * Description: results from fuzzy overlay without planned land use considered. 

* /results/Suitability_results_rast.jpg
    * Format: jpeg
    * Description: weighted sum results with unequal weights considered.

* /results/Suitability_results_noweight.jpg
    * Format: jpeg
    * Description: weighted sum results with equal weights considered.

* /results/Suitability_results_avg.jpg
    * Format: jpeg
    * Description: weighted sum results with average suitability score compute for each census tract. 

* /code/Analyze_Businesses.ipynb
    * Format: IPYNB
    * Description: script to analyze data and perform fuzzy overlay and weighted sum. 
* /code/Analyze_Businesses
    * Format: PDF
    * Description: script to analyze data and perform fuzzy overlay and weighted sum. 

* /code/Clean_Data.ipynb
    * Format: IPYNB
    * Description: script to clean data and join demographics to census tract geometries. 

* /code/Clean_Data
    * Format: PDF
    * Description: script to clean data and join demographics to census tract geometries. 

* /code/Get_Data.ipynb
    * Format: IPYNB
    * Description: script to obtain data from Google Places API and MN Geospatial Commons.

* /code/Get_Data
    * Format: PDF
    * Description: script to obtain data from Google Places API and MN Geospatial Commons.
