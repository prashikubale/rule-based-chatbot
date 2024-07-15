import random
import re
import datetime
class GenesisBot:
    # negative response
    negative_responses = ("no","nope","nahi","sorry")
    # positive response
    positive_responses = ("yeah","yay","yes")
    #exit kke liye
    exit_commands =  ("bye","pause","exit")

    random_questions = (
        "hey how can i help you today",
        "you need me?, ask me anything",
        "any special problem this time?",
        "hey user what could i help you this time"
    )

    def __init__(self):
        self.bank_intents = {
            'check_balance_intent': r'.*\b(check|balance|account)\b.*',
            'check_ticket_intent': r'.*\b(check|ticket|account)\b.* Is Your Tracking ID',
            'track_ticket_intent': r'.*\b(check|balance|account)\b.*',
            'about_session': r'.*\s*session'
        }

    def greet(self):
        self.name = input("Hey user How are you?\n")
        will_help = input(f"Hi {self.name}, I am Genesis. Will you let me know your problem?\n")
        if will_help in self.negative_responses:
            print("Ok, have a nice day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands :
            if reply == command:
                print("chal bhay me jara")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while True:
            if self.make_exit(reply):
                break
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.bank_intents.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply, re.IGNORECASE)
            if found_match and intent == 'check_balance_intent':
                return self.check_balance_intent()
            elif found_match and intent == 'check_ticket_intent':
                return self.check_ticket_intent()
            elif found_match and intent == 'track_ticket_intent':
                return self.track_ticket_intent()
            elif found_match and intent == 'about_session':
                return self.about_session()
        return self.no_match_intent()

    def check_balance_intent(self):
        responses = ("Here is your account balance...\n",
                     "This is your account balance..\n")
        return random.choice(responses)

    def check_ticket_intent(self):
        responses = ("your ticket id is...\n",
                     "here is you ticket id....\n")
        return random.choice(responses)

    def track_ticket_intent(self):
        return "I didn't understand that. Can you please rephrase?"

    def about_session(self):
        today = (datetime.datetime.today())
        return f"Today is {today}"
    
    def no_match_intent(self):
        return "I didn't understand that. Can you please rephrase?"

Genesis = GenesisBot()    
Genesis.greet()