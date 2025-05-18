import random

def get_message_cli(current_language, translations, key, **kwargs): # Renamed to avoid conflict if we want separate CLI/GUI get_message
    message_template = translations.get(current_language, translations["en"]).get(key, translations["en"].get(key))
    if message_template is None:
        return key 
    return message_template.format(**kwargs)

def set_language_cli(current_language, translations):
    """Allows the user to select a language for CLI."""
    lang_code = input(translations["en"]["select_language_prompt"]).strip().lower()
    if lang_code in translations:
        current_language = lang_code
    else:
        print(translations["en"]["language_not_supported"].format(lang=lang_code))
        current_language = "en" 

def main_cli(current_language, translations, winners, names_list):
    while True:
        name_input = input(
            get_message_cli(
                current_language,
                translations,
                "enter_name_prompt", 
                quit_cmd=get_message_cli(current_language, translations, "quit_command"), 
                next_cmd=get_message_cli(current_language, translations, "next_command")
                )
            )
        if name_input.lower() == get_message_cli(current_language, translations, "quit_command"):
            print(get_message_cli(current_language, translations, "exiting_program"))
            break
        elif name_input.lower() == get_message_cli(current_language, translations, "next_command"):
            if not names_list:
                print(get_message_cli(current_language, translations, "no_names_to_select"))
            else:
                selected_winner_name = make_selection(current_language, translations, names_list)
                if selected_winner_name:
                    winner(current_language, translations, winners, names_list, selected_winner_name)
        else:
            names_list.append(name_input)
            print(get_message_cli(current_language, translations, "name_added_to_list", name=name_input))

def make_selection(current_language, translations, current_names):
    if not current_names:
        print(get_message_cli(current_language, translations, "no_names_to_select"))
        return None
    
    selected_name = random.choice(current_names)
    print(get_message_cli(current_language, translations, "congratulations_winner", name=selected_name))
    current_names.remove(selected_name)
    return selected_name

def winner(current_language, translations, winners, names, name_of_the_winner):
    if name_of_the_winner is None:
        print(get_message_cli(current_language, translations, "error_no_winner_provided"))
        return

    winners.append(name_of_the_winner)
    print(get_message_cli(current_language, translations, "added_to_winners_list", name=name_of_the_winner))

    if not names: # Check the global names list
        print(get_message_cli(current_language, translations, "game_over_all_selected", winners_list=winners))
    else:
        print(get_message_cli(current_language, translations, "names_remaining", count=len(names)))
