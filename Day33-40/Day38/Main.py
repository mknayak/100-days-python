from datetime import  datetime
import requests
import os

NUTRITIONIX_APP_KEY= "b891dca5ea70597ee3b1becb8058a50b"
NUTRITIONIX_APP_ENDPOINT= "https://trackapi.nutritionix.com/v2/"


def get_nutrients_info(text):
    headers={"x-app-id": os.environ["NUTRIENT_APP_ID"],
             "x-app-key": NUTRITIONIX_APP_KEY}
    path="natural/exercise"
    body={"query": text}
    response = requests.post(url=f"{NUTRITIONIX_APP_ENDPOINT}{path}",json=body,headers=headers)
    api_response= response.json()
    exercise_list=api_response["exercises"]
    print(exercise_list)
    return exercise_list

def write_exercise_list_to_google_sheet(exercise_list):
    API="https://api.sheety.co/9769300c2cb0b0ac26f71741c7dfcf00/manasWorkouts/workouts"
    AUTH_TOKEN="pythontesttoken"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "content-type": "application/json"}

    for exercise in exercise_list:
        data = {
            "workout":{
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["user_input"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(url=API, json=data, headers=headers)
        api_response= response.json()
        print(api_response)


user_input = input("Tell me what you did today:")

exercises_list = get_nutrients_info(user_input)
write_exercise_list_to_google_sheet(exercises_list)
