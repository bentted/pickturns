# Turn Picker / Name Selector Application

This Python application provides a fun and easy way to randomly select a name from a list. It can be used for picking turns, choosing winners, or any other scenario where a random selection is needed. The application supports multiple languages and offers both a Command-Line Interface (CLI) and a Graphical User Interface (GUI).

## Features

*   **Random Name Selection:** Fairly selects a name from a user-provided list.
*   **Multiple Entries:** Allows adding multiple names to the selection pool.
*   **Winner Tracking:** Keeps track of selected names (winners) and can display the list of all winners once all names have been selected.
*   **Multilingual Support:** 
    *   The application interface (both CLI and GUI) can be switched to various languages.
    *   Currently supported languages include: English (en), Spanish (es), German (ger), French (fr), Italian (it), Portuguese (pt), Dutch (nl), Polish (pl), Swedish (sv), Greek (el), Russian (ru), Japanese (ja), Korean (ko), Hindi (hi), Arabic (ar), Turkish (tr), Vietnamese (vi), Thai (th), Hebrew (he), Swahili (sw), Hausa (ha), Yoruba (yo), Zulu (zu), Amharic (am), Simplified Chinese (zh-CN), and Traditional Chinese (zh-TW).
*   **Dual Interface:**
    *   **CLI (Command-Line Interface):** For users who prefer text-based interaction.
    *   **GUI (Graphical User Interface):** A user-friendly visual interface built with Tkinter.
*   **Persistent Winners List (GUI):** In the GUI, even after all names are picked, the list of winners remains displayed.
*   **Dynamic UI Updates:** The GUI language can be changed on-the-fly, and all text elements will update immediately.

## Prerequisites

*   Python 3.x
*   Tkinter (usually included with Python standard library)

## How to Run

1.  **Download:** Get the `turnpicker.py` file.
2.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the file (`c:\Users\ruess\OneDrive\Desktop\` in this case).
3.  **Execute the script:**
    ```bash
    python turnpicker.py
    ```

By default, this will launch the **GUI version** of the application.

### Running the GUI Version

When you run `python turnpicker.py`, the graphical interface will appear.

*   **Language Selection:**
    *   Use the dropdown menu at the top to select your preferred language. The UI will update instantly.
*   **Adding Names:**
    *   Type a name into the "Enter a Name" (or its translated equivalent) input field.
    *   Click the "Add Name" button. A confirmation message will appear.
*   **Selecting a Name/Winner:**
    *   Click the "Select Name" button.
    *   A randomly selected name will be displayed as the winner. This name is removed from the selection pool and added to a list of winners.
*   **Game Over:**
    *   Once all names have been selected, a "Game is over!" message will be displayed along with an enumerated list of all winners in the order they were picked.
    *   If you try to select a name when the list is empty (either initially or after all names are picked), an appropriate message will be shown.

### Running the CLI Version

To run the Command-Line Interface version, you need to modify the `turnpicker.py` script slightly.

1.  Open `turnpicker.py` in a text editor.
2.  Scroll to the very bottom of the file, to the `if __name__ == "__main__":` block.
3.  Comment out the line that runs the GUI:
    ```python
    # To run GUI version:
    # root.mainloop() 
    ```
4.  Uncomment the lines that run the CLI:
    ```python
    # To run CLI version:
    set_language_cli() 
    main_cli(names)
    ```
5.  Save the file.
6.  Now, run the script from your terminal:
    ```bash
    python turnpicker.py
    ```

*   **Language Selection (CLI):**
    *   The first prompt will be: `Select language (e.g., en, es):`
    *   Enter the language code (e.g., `es` for Spanish, `fr` for French). If an unsupported code is entered, it will default to English.
*   **Adding Names (CLI):**
    *   You'll be prompted to `Enter your name (or type 'quit' to exit, 'next' to select a name):` (message will be in the selected language).
    *   Type a name and press Enter. A confirmation message will be shown.
*   **Selecting a Name/Winner (CLI):**
    *   At the prompt, type `next` (or its translated equivalent for the `next_command`) and press Enter.
    *   A winner will be randomly selected and announced.
    *   The application will also show how many names remain.
*   **Exiting (CLI):**
    *   At the prompt, type `quit` (or its translated equivalent for the `quit_command`) and press Enter.
*   **Game Over (CLI):**
    *   When all names have been selected, a "Game is over!" message will be displayed with the list of winners.

## Code Structure Overview

*   **`translations` Dictionary:** Contains all the text strings for different languages. Each language has a code (e.g., "en", "es") as a key.
*   **`current_language` Variable:** Stores the currently active language code.
*   **`get_message(key, **kwargs)`:** Retrieves translated strings for the GUI. It falls back to English if a translation is missing for the current language or if the key itself is not found in English.
*   **GUI Functions (`add_name_ui`, `select_name_ui`, `update_ui_language`, `on_language_select`):** Manage the logic for the Tkinter graphical interface.
*   **Tkinter Widgets:** Standard Tkinter elements (labels, buttons, entry fields, combobox) are used to build the GUI. Styling is applied for a more modern look.
*   **CLI Functions (`get_message_cli`, `set_language_cli`, `main_cli`, `make_selection`, `winner`):** Handle the logic for the command-line interface.
*   **`names` List:** Stores the list of names entered by the user.
*   **`winners` List:** Stores the list of names that have been selected.
*   **`if __name__ == "__main__":` Block:** The entry point of the script. It's configured to run either the GUI or the CLI version (requires manual editing to switch).

## Contributing

Contributions are welcome, especially for adding or improving translations!

### Adding/Improving Translations

1.  **Open `turnpicker.py`**.
2.  **Locate the `translations` dictionary** near the top of the file.
3.  **Find the language code** you want to edit or add. Language codes are typically two-letter ISO 639-1 codes (e.g., `fr` for French, `de` for German). For Chinese, `zh-CN` (Simplified) and `zh-TW` (Traditional) are used.
4.  **Edit existing translations:** If you see a string that's incorrect or could be improved for a specific language, simply change its value.
5.  **Adding a new language:**
    *   If the language is not present, add a new entry to the `translations` dictionary. For example, to add Klingon (`tlh`):
        ```python
        "tlh": { # Klingon translations
            "select_language_prompt": "tlh: Select language (e.g., en, tlh): ",
            "language_not_supported": "tlh: Language '{lang}' not supported. Using English.",
            "enter_name_prompt": "tlh: Enter your name (or type '{quit_cmd}' to exit, '{next_cmd}' to select a name): ",
            "exiting_program": "tlh: Exiting the program.",
            "no_names_to_select": "tlh: No names to select from. Please add some names first.",
            "name_added_to_list": "tlh: '{name}' added to the list.",
            "congratulations_winner": "tlh: Congratulations {name}! You are the winner!",
            "error_no_winner_provided": "tlh: Error: No winner was provided to the winner function.",
            "added_to_winners_list": "tlh: '{name}' has been added to the winners list.",
            "game_over_all_selected": "tlh: Game is over! All names have been selected. The winners are: {winners_list}",
            "names_remaining": "tlh: There are {count} names remaining in the selection pool.",
            "quit_command": "tlh: quit",
            "next_command": "tlh: next",
            "app_title": "tlh: Name Selector",
            "enter_name_label": "tlh: Enter a Name:",
            "select_name_button": "tlh: Select Name",
            "add_name_button": "tlh: Add Name",
            "status_initial": "tlh: Add names and click 'Select Name'.",
            "language_dropdown_label": "tlh: Language:",
            "enter_name_prompt_ui": "tlh: Please enter a name to add."
        },
        ```
    *   Ensure you translate all the keys present in the English (`"en"`) dictionary entry. Pay attention to placeholders like `{name}`, `{lang}`, `{quit_cmd}`, `{next_cmd}`, `{count}`, and `{winners_list}` – these should be kept in the translated strings as they are replaced dynamically by the program.
6.  **Test your changes:** Run the application (both GUI and CLI if possible) and select the language you modified to ensure everything appears correctly.
7.  If you're contributing via a platform like GitHub, submit a pull request with your changes.

### Other Contributions

Feel free to suggest or implement new features, bug fixes, or code improvements.

## Technology Used

*   **Python:** The core programming language.
*   **Tkinter:** Python's standard GUI (Graphical User Interface) package, used for the visual interface.
*   **random module:** Used for the random selection of names.

---

