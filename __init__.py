from mycroft import MycroftSkill, intent_file_handler


class Focus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('focus.intent')
    def handle_focus(self, message):
        self.speak_dialog('focus')


def create_skill():
    return Focus()

