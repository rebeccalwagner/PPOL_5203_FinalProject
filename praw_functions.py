from datetime import datetime
import pandas as pd

############################################################################################################################################

def search_subreddit(subreddit, query:str, limit:int):
    """query a specific subreddit.
    query: string query for praw api
    limit: int number of threads to collect
    returns: dataframe of threads matching query"""

    thread_list = list() # init list for thread data

    for submission in subreddit.search(query=query, limit=limit): # iterate over all threads returned from search

        # grab year and month from thread
        date = datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        year = date.split("-")[0]
        month = date.split("-")[1]

        result_dict = { # put thread data in a dict
                "submission_id":submission.id,
                "title":submission.title,
                "text":submission.selftext,
                "year":year,
                "month":month
        }

        thread_list.append(result_dict) # append dict to list

    df = pd.DataFrame(thread_list) # turn list into dataframe
    df.set_index("submission_id", inplace=True) # set index to be thread id

    return df

############################################################################################################################################

def get_comments(id_list:list, reddit):
    """get all comments from a specific thread
    id_list: list of submission ids to get comment data from
    reddit: reddit instance 
    returns: dataframe of comment data"""
    
    comments_list = list()

    for id in id_list:
        
        submission = reddit.submission(id=id)
        submission.comments.replace_more(limit=None) # expand all comments as much as possible

        for comment in submission.comments.list():

            date = datetime.fromtimestamp(comment.created_utc).strftime("%Y-%m-%d %H:%M:%S")
            year = date.split("-")[0]
            month = date.split("-")[1]

            comment_dict = {
                "submission_id": id,
                "author": comment.author.name if comment.author else None,
                "body": comment.body,
                "score": comment.score,
                "year":year,
                "month":month
            }   

            comments_list.append(comment_dict)

    df = pd.DataFrame(comments_list)

    return df

############################################################################################################################################