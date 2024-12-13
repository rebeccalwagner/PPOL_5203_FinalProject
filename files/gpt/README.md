For Replication:
1. Run scraped reddit files through `run_gpt_api` to code for safety relevance and sentiment analysis in small batches. 
2. Combine output files using `combine_coded_data`
3. Clean the resulting single file using `clean_gpt_output`

 File name    | Use case |
| -------- | ------- |
| clean_gpt_output | drop all non relevent data from the combined csv output file |
| code_test_set | manually code reddit comments     |
| combine_coded_data | combine all csv files containing reddit comments coded by chat gpt through `run_gpt_api` |
| split_nan | split comments with gpt output nan from propertly coded comments    |
| run_gpt_api_test | code with testing of gpt api   |
| gpt_test | prompt engineer with gpt for highest accuracy |
| run_gpt_api | have chat gpt decide what reddit data is safety related & preform sentiment analysis    |