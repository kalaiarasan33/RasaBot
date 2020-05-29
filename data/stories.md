## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy


<!-- example utterance -->
## HelloWorld path
* HelloWorld
  - utter_HelloWorld


<!-- example action -->

## devops path
* devops
  - action_devops



<!-- example entities extraction -->

## userdetails path
* userdetails
  - action_userdetails


<!-- example entities extraction -->

## covidtracker path
* covidtracker
  - action_covidtracker

<!-- Sample multi slot test -->
## slottest path
* slottest
  - utter_slottest


<!-- custom multi slot test -->
## customslottest path
* customslottest
  - utter_customslottest_greet
* name_entity
  - utter_name_entity_greet
* country_entity
  - utter_country_entity
  - action_customslottest
  - utter_leader_bye


<!-- Git Repo test with form -->

## customslottestdevops path
* customslottestdevops
  - utter_customslottestdevops_greet
* devopsformtest
  - devops_form
  - form{"name": "devops_form"}
  - form{"name": null}
  - utter_customslottestdevops_slot_values


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
