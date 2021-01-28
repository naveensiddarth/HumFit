# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import ast
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

class RecipeForm(FormAction):

     def name(self) -> Text:
         return "recipe_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
          
          return["cuisine","type","course"]
     
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
          return {
               "cuisine": [
                    self.from_entity(entity="cuisine", intent=["telling_cuisine"]),
               ],
               "type": [
                    self.from_entity(entity="type", intent=["telling_type"]),
               ],
               "course": [
                    self.from_entity(entity="course", intent=["telling_course"]),
               ],
          }
     
