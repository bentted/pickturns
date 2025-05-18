import random

class CLI:
    def __init__(self, current_language, translations, winners, names):
        self.current_language = current_language
        self.translations = translations
        self.winners = winners
        self.names = names

    def get_message_cli(self, key, **kwargs): # Renamed to avoid conflict if we want separate CLI/GUI get_message
        message_template = self.translations.get(
            self.current_language, self.translations["en"]
            ).get(key, self.translations["en"].get(key))
        if message_template is None:
            return key 
        return message_template.format(**kwargs)

    def set_language_cli(self):
        """Allows the user to select a language for CLI."""
        lang_code = input(self.translations["en"]["select_language_prompt"]).strip().lower()
        if lang_code in self.translations:
            self.current_language = lang_code
        else:
            print(self.translations["en"]["language_not_supported"].format(lang=lang_code))
            self.current_language = "en" 

    def main_cli(self):
        while True:
            name_input = input(
                self.get_message_cli(
                    "enter_name_prompt", 
                    quit_cmd=self.get_message_cli("quit_command"), 
                    next_cmd=self.get_message_cli("next_command")
                    )
                )
            if name_input.lower() == self.get_message_cli("quit_command"):
                print(self.get_message_cli("exiting_program"))
                break
            elif name_input.lower() == self.get_message_cli("next_command"):
                if not self.names:
                    print(self.get_message_cli("no_names_to_select"))
                else:
                    selected_winner_name = self.make_selection(self.names)
                    if selected_winner_name:
                        self.winner(selected_winner_name)
            else:
                self.names.append(name_input)
                print(self.get_message_cli("name_added_to_list", name=name_input))

    def make_selection(self, current_names):
        if not current_names:
            print(self.get_message_cli("no_names_to_select"))
            return None
        
        selected_name = random.choice(current_names)
        print(self.get_message_cli("congratulations_winner", name=selected_name))
        current_names.remove(selected_name)
        return selected_name

    def winner(self, name_of_the_winner):
        if name_of_the_winner is None:
            print(self.get_message_cli("error_no_winner_provided"))
            return

        self.winners.append(name_of_the_winner)
        print(self.get_message_cli("added_to_winners_list", name=name_of_the_winner))

        if not self.names:
            print(self.get_message_cli("game_over_all_selected", winners_list=self.winners))
        else:
            print(self.get_message_cli("names_remaining", count=len(self.names)))
