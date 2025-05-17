# Turn Picker Application

## Overview

The Turn Picker application is a versatile desktop tool built with Python and Tkinter. It provides a collection of utilities designed to assist with various turn-based activities, tabletop games, and decision-making processes. The application features a user-friendly interface with support for multiple languages.

## Features

*   **Multi-Language Support:** The UI and content can be displayed in multiple languages, including:
    *   English (en)
    *   Spanish (es)
    *   French (fr)
    *   German (de)
    *   Japanese (ja)
    *   Chinese (zh)
    *   Korean (ko)
    *   Italian (it)
    *   Portuguese (pt)
    *   Russian (ru)
*   **Name Selector:** Allows users to input a list of names and randomly select one. It also keeps track of previously picked names.
*   **Dice Roller:** A flexible dice rolling utility that supports:
    *   Rolling 1 to 10 dice simultaneously.
    *   Standard dice types: d4, d6, d8, d10, d12, d20, d100.
    *   Display of individual die results and the total sum.
*   **D&D Helper:** A dedicated screen for Dungeons & Dragons players, featuring:
    *   Input fields for character name, class, and level.
    *   An initiative roller.
    *   Display area for character details and initiative roll results.
*   **Card Game Helper:** A new module to assist with card games:
    *   Dropdown menu to select from a list of popular card games (e.g., Poker, Blackjack, Uno, Bridge, Rummy, Solitaire, Go Fish, War, Crazy Eights, Spades).
    *   Display area for the rules of the selected card game.
    *   Card game rules are translatable and can be displayed in the selected application language.

## Requirements

*   Python 3.x
*   Tkinter library (typically included with standard Python installations)

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Save the `turnpicker.py` script to a directory on your computer.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Execute the script using the command:
    ```bash
    python turnpicker.py
    ```

## Application Screens and Usage

### Main Window & Language Selection

Upon launching the application, the main window appears.
*   **Language Dropdown:** Located at the top, this dropdown allows you to change the display language of the entire application dynamically.
*   **Navigation Buttons:** Buttons to switch to the different helper screens:
    *   "Name Selector"
    *   "Dice Roller"
    *   "D&D Helper"
    *   "Card Game Helper"

### 1. Name Selector Screen

*   **Functionality:** Helps in randomly picking a name from a user-defined list.
*   **UI Elements:**
    *   **Name Entry Field:** Input names one by one.
    *   **Add Name Button:** Adds the entered name to the list.
    *   **Pick Name Button:** Randomly selects a name from the current list. The selected name is displayed.
    *   **Clear List Button:** Empties the list of names.
    *   **Current List Display:** Shows all names currently in the list.
    *   **Previously Picked Display:** Shows names that have already been picked in the current session.
    *   **Back Button:** Returns to the main navigation screen.

### 2. Dice Roller Screen

*   **Functionality:** Simulates rolling various types of polyhedral dice.
*   **UI Elements:**
    *   **Number of Dice Dropdown:** Select how many dice to roll (1 to 10).
    *   **Number of Sides Dropdown:** Select the type of dice (d4, d6, d8, d10, d12, d20, d100).
    *   **Roll Dice Button:** Executes the dice roll.
    *   **Results Display Area:** Shows the outcome of each individual die roll and the sum of all rolls.
    *   **Back Button:** Returns to the main navigation screen.

### 3. D&D Helper Screen

*   **Functionality:** Assists Dungeons & Dragons players with character information and initiative rolls.
*   **UI Elements:**
    *   **Character Name Entry:** Field to input the character's name.
    *   **Character Class Entry:** Field to input the character's class.
    *   **Character Level Entry:** Field to input the character's level.
    *   **Roll Initiative Button:** Calculates and displays an initiative roll (typically 1d20 + modifiers, though the current version might be a simple d20 roll).
    *   **Display Area:** Shows the entered character details and the result of the initiative roll.
    *   **Back Button:** Returns to the main navigation screen.

### 4. Card Game Helper Screen

*   **Functionality:** Provides rules for various card games.
*   **UI Elements:**
    *   **Screen Title:** "Card Game Helper".
    *   **Select Card Game Label & Dropdown:** Allows users to choose a card game from a predefined list:
        *   Poker
        *   Blackjack
        *   Uno
        *   Bridge
        *   Rummy
        *   Solitaire
        *   Go Fish
        *   War
        *   Crazy Eights
        *   Spades
    *   **Card Game Rules Title Label:** "Rules:".
    *   **Rules Display Area (Text Widget):** Shows the rules for the selected card game in the currently active application language. If a translation is not available for a specific game in the selected language, it defaults to English.
    *   **Back Button:** Returns to the main navigation screen.

## Internationalization (i18n)

The application is designed to be easily translatable.

### UI Text Translations

*   All UI text elements (labels, button texts, titles) are stored in a nested dictionary named `translations` within `turnpicker.py`.
*   The structure is `translations[language_code][key] = "Translated Text"`.
    *   Example: `translations['es']['app_title'] = "Selector de Turnos"`
*   To add or modify translations:
    1.  Identify the language code (e.g., `'fr'` for French).
    2.  Find the appropriate key for the UI element (e.g., `'name_selector_title'`).
    3.  Add or update the entry in the `translations` dictionary.

### Card Game Rules Translations

*   Card game rules are stored in a separate nested dictionary named `card_game_rules_translations`.
*   The structure is `card_game_rules_translations[language_code][game_name] = "Translated Rules Text"`.
    *   Example: `card_game_rules_translations['fr']['Poker'] = "Règles du Poker..."`
*   To add or update rule translations:
    1.  Ensure the `game_name` matches exactly with the names in `card_games_list`.
    2.  Add the translated rules under the appropriate language code and game name.
    3.  The application will automatically pick up these translations when the language or game selection changes. If a translation is missing for the current language, it defaults to English rules.

## Code Structure (Brief)

*   **Main Script:** `turnpicker.py` contains all the application logic, UI definitions, and translation data.
*   **GUI:** Built using the Tkinter library (`tk` and `ttk` modules).
*   **Core Data Structures for i18n:**
    *   `translations`: For general UI text.
    *   `card_game_rules_translations`: For card game rules.
*   **Functions:**
    *   `update_ui_language()`: Handles dynamic updating of all display text when the language is changed.
    *   Separate functions `show_name_selector_frame()`, `show_dice_roller_frame()`, `show_dnd_helper_frame()`, `show_card_game_frame()` manage the display of different screens.
    *   `show_card_game_rules()`: Updates the rules display in the Card Game Helper based on selection and language.

## Contributing

Contributions are welcome! Here are some ways you can help:

*   **Add More Card Games:**
    1.  Add the game name to the `card_games_list` in `turnpicker.py`.
    2.  Add the rules for the new game (in English) to `card_game_rules_translations['en']`.
*   **Translate Card Game Rules:** Provide translations for existing or new card game rules in the `card_game_rules_translations` dictionary for various languages.
*   **Translate UI Text:** Add or improve translations in the `translations` dictionary for any of the supported (or new) languages.
*   **Improve UI/UX:** Suggest or implement improvements to the user interface or user experience.
*   **Add New Features:** Propose and/or develop new helper tools for the application.
*   **Report Bugs:** If you find any issues, please report them.

## License

This project is open source. (You may want to add a specific license like MIT, GPL, etc., if you decide to choose one).

