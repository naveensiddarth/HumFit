stories:
    - story: show recipes
     steps:
     - intent: greet
     - action: utter_greet
     - action: utter_ask_re
     - intent: choose_recipes
     - action: utter_ask_cuisine
     - intent: telling_cuisine{"cuisine": "Italian"}
     - action: utter_ask_type
     - intent: telling_type{"type": "Vegetarian"}
     - action: utter_ask_course
     - intent: telling_course{"course": "Breakfast"}
     - action: action_show_recipes
     - action: utter_gratitude

    - story: show exercises
      steps:
      - intent: greet
      - action: utter_greet
      - action: utter_ask_re
      - intent: choose_exercises
      - action: utter_ask_muscles
      - intent: telling_muscles{"muscles": "Abs"}
      - action: action_show_exercises
      - action: utter_gratitude
