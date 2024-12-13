# PPOL_5203_FinalProject

Read original proposal `Data_Science_Final_Proposal.pdf`

## Repo Organization

| parent folder | sub folder | description |
|---------------|------------|-------------|
| files | reddit_scraping | contains all .py and .ipynb files used to scrape and clean reddit data |
| files | gpt | contains all .py and .ipynb files used to call GPT API to classify and preform sentiment analysis on reddit data |
| files | analysis | contains all .py and .ipynb files used to analyze imported and collected data |
| data | open_data_dc | contains data imported from OpenDataDc |
| data | reddit | contains all data scraped from reddit |
| data | zillow | contains all data imported from Zillow |
| Figures | | contains figures produced for final analysis |

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


