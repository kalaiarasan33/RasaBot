# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class Actiondevops(Action):

    def name(self) -> Text:
        return "action_devops"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = "Git,Jenkins,Ansible,AWS,Python"

        dispatcher.utter_message(text=a)

        return []

class Actionuser(Action):

    def name(self) -> Text:
        return "action_userdetails"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities= tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity'] == 'name':
                name = e['value']
                if name == 'kalai':
                    a = "kalai is devops engineer"
                if name == 'chandru':
                    a = "chandru is ui developer"
                if name == 'kishore':
                    a = "kishore is school student"

        dispatcher.utter_message(text=a)

        return []


class Actioncovidtracker(Action):

    def name(self) -> Text:
        return "action_covidtracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()
        entities= tracker.latest_message['entities']
        print(entities)
        state = None
        for e in entities:
            if e['entity'] == 'state':
                state = e['value']
        message = "Enter the state name properly"
        for data in response['statewise']:
            if data['state'] == state.title():
                print(data)
                message = "Active: " + data['active'] + " confirmed: " + data['confirmed'] + " death: "  + data['deaths'] + " deltarecovered: " + data["deltarecovered"]


        dispatcher.utter_message(text=message)

        return []

class Actionslottest(Action):

    def name(self) -> Text:
        return "action_customslottest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        name = tracker.get_slot("name")
        country = tracker.get_slot("country")
        leader_name =""
        if country.lower() == 'india':
            leader_name = "Modi"
        if country.lower() == 'us':
            leader_name = "Trump"



        dispatcher.utter_message(text=f"your {name} and belongs to {country} and leader name is {leader_name}")

        return [SlotSet("leader",leader_name)]

class Actionsdevops(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "devops_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["project", "repo", "action"]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []

class Actioncovidtracker(Action):

    def name(self) -> Text:
        return "action_covidtracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()
        entities= tracker.latest_message['entities']
        print(entities)
        state = None
        for e in entities:
            if e['entity'] == 'state':
                state = e['value']
        message = "Enter the state name properly"
        for data in response['statewise']:
            if data['state'] == state.title():
                print(data)
                message = "Active: " + data['active'] + " confirmed: " + data['confirmed'] + " death: "  + data['deaths'] + " deltarecovered: " + data["deltarecovered"]


        dispatcher.utter_message(text=message)

        return []
