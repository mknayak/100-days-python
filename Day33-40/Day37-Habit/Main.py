from datetime import datetime, timedelta

import requests
ENDPOINT = "https://pixe.la/v1"
USERNAME = "manasmk"
TOKEN="adsjdkjhLKJHDSJOhiuads"
GRAPH_ID="code-graph"
GRAPH_NAME="Coding Habit"
def create_user(username):
    user_endpoint=f"{ENDPOINT}/users"
    user_params = {
        "username":username,
        "token":TOKEN,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }
    response = requests.post(user_endpoint, json=user_params).json()
    print(response)
    return response

def create_graph(graph_id, graph_name):
    graph_endpoint=f"{ENDPOINT}/users/{USERNAME}/graphs"
    graph_params = {
        "id":graph_id,
        "name":graph_name,
        "unit":"Hour",
        "type":"int",
        "color":"kuro"}
    headers = {"X-USER-TOKEN":TOKEN}
    response = requests.post(graph_endpoint, json=graph_params, headers=headers).json()
    print(response)
    return response

def post_value_to_graph(date:datetime,value):
    graph_post_endpoint=f"{ENDPOINT}/users/{USERNAME}/graphs/code-graph"
    graph_post_params = {"date":date.strftime("%Y%m%d") , "quantity":f"{value}" }
    headers = {"X-USER-TOKEN":TOKEN}
    response = requests.post(graph_post_endpoint, json=graph_post_params, headers=headers).json()
    print(response)
    return response

def update_value_to_graph(graphid,date:datetime,value):
    graph_post_endpoint=f"{ENDPOINT}/users/{USERNAME}/graphs/{graphid}/{date.strftime("%Y%m%d")}"
    graph_post_params = {"quantity":f"{value}" }
    headers = {"X-USER-TOKEN":TOKEN}
    response = requests.put(graph_post_endpoint, json=graph_post_params, headers=headers).json()
    print(response)
    return response

#create_user(USERNAME)
#create_graph(GRAPH_ID,GRAPH_NAME)
#post_value_to_graph(datetime.today()+timedelta(days=1), 12)
update_value_to_graph(GRAPH_ID,datetime.today(), 4)

