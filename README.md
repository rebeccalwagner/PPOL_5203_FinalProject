## Reddit vs. Reality: Online Perceptions of Neighborhood Safety in Washington, D.C
### Rebecca Wagner & Elizabeth Bagely, McCourt School of Public Policy 

Cities all over the United States are battling the process of gentrification within their neighborhoods. This process causes both
housing prices to increase, and crime rates to decrease. Additionally, public perceptions of crime have generally increased in
many cities, despite crime rates falling nationwide. In this project, we attempt to better understand the relationship between
perceptions of crime, true reported rates of crime, and housing markets, in an effort to untangle the many factors at play in
gentrification. To do so, we focus specifically on the city of Washington, D.C, and utilize public datasets on crime rates and
housing prices. We also collect our own dataset from social media platform Reddit through its API to create a quantification of
public safety sentiment. We ultimately find that trends in perceived safety appear to lag behind changes in true crime rates, and
that online safety sentiments and housing prices appear to be correlated, though more analysis is needed to parse the nature
of this relationship.

## Repo Organization

| parent folder | sub folder | description |
|---------------|------------|-------------|
| files | reddit_scraping | contains all .py and .ipynb files used to scrape and clean reddit data |
| files | gpt | contains all .py and .ipynb files used to call GPT API to classify and preform sentiment analysis on reddit data |
| files | analysis | contains all .py and .ipynb files used to analyze imported and collected data |
| data | open_data_dc | contains data imported from OpenDataDc |
| data | reddit | contains all data scraped from reddit |
| data | zillow | contains all data imported from Zillow |
| figures | | contains figures produced for final analysis |

## Project Walkthrough 

### Reddit Data Collection 

All reddit data regarding public safety sentiment was scraped from three subreddits: r/washingtondc, r/wasdc, aand r/DCforRent. Files for scraping and cleaning this data can be found in `files/reddit_scraping`

1. Scrape Reddit data using the three `get_reddit` notebooks. Functions are pulled from `praw_functions.py`. Each outputs two csv files, one for threads and one for comments. 

2. Clean & combine scraped reddit csv files using `cleaning_reddit_data.ipynb`

3. Search for and drop any commments that are obviously not safety related using `remove_non_starters.ipynb`

### GPT Classification and Sentiment Analysis

Cleaned and scraped Reddit data was classified as either safety related or not safety related. Sentiment analysis was preformed on all safety related comments. Files used to classify reddit data and preform sentiment analysis through ChatGPT API can be found in `files/gpt`

1. Run scraped reddit files through `run_gpt_api` to code for safety relevance and sentiment analysis in small batches. 

2. Combine output files using `combine_coded_data`

3. Clean the resulting single file using `clean_gpt_output`

### Analysis 

1. Map crime data into neighborhoods using `add_crime_neighborhoods` notebook. Requries shape files for neighborhoods from Zillow and Open Data DC Crime states. Outputs crime data with neighborhoods csv

2. Extract neighborhoods from Reddit data using `neighborhood matching` notebook. Requries cleaned sentiment data and all threads data. Outputs sentiment with neighborhoods csv

3. Map Zip codes, neighborhood clusters, and neighborhoods using `spacial matching csv`. Requires Zillow shape files. Outputs geo matching csv

4. Create Vizualizations and Regression Model with `lag_model`, `open_data_dc_viz`, `sentiment_figures`, etc. 
5. 


