# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionShowRecipes(Action):

    def name(self) -> Text:
        return "action_show_recipes"

    def  run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        response = requests.get().json()
        entities = tracker.latest_message['entities']
        cuisine = None
        type = None
        course = None
        for e in entities:
            if e['entity'] == "cuisine":
                cuisine = e['value']
            if e['entity'] == "type":
                type = e['value']
            if e['entity'] == "course":
                course = e['value']
       for data in response["Recipes"]:
           if data["Cuisine"] ==  cuisine.title() && data["Type"] == type.title() && data["Course"] == course.title():
               print(data)
               message =  data["Name"] + data["PrepTime"] + data["TotalTime"] + data["Calories"] + data["Instructions"]
               dispatcher.utter_message(message)

class ActionShowExercices(Action):

    def name(self) -> Text:
        return "action_show_exercises"

    def  run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        response = requests.get().json()
        entities = tracker.latest_message['entities']
        muscle = None
        for e in entities:
            if e['entity'] == "muscle":
                muscle = e['value']
       for data in response["Exercises"]:
           if  data["Muscle"] == muscle.title():
               print(data)
               message =  data["Name"] + data["Muscle"] + data["SecondaryMuscle"] + data["Instructions"]
               dispatcher.utter_message(message)
