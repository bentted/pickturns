# Turn Picker

A Python script that allows users to create a list of names and then randomly select a "winner" from that list. The script supports multiple languages for its user interface prompts.

## Features

*   **Add Names:** Users can dynamically add names to a list.
*   **Random Selection:** Randomly picks a name from the current list.
*   **Winner Tracking:** Keeps a list of names that have already been selected.
*   **Multilingual Support:** User prompts and messages can be displayed in various languages. The user is prompted to select a language at the start.
*   **Game Over Notification:** Informs the user when all names from the list have been selected.
*   **Remaining Names Count:** Shows how many names are left in the selection pool after each pick.

## How to Run

1.  **Save the script:** Ensure you have the `turnpicker.py` file.
2.  **Open a terminal or command prompt.**
3.  **Navigate to the directory** where you saved the `turnpicker.py` file.
4.  **Run the script** using the command:
    ```bash
    python turnpicker.py
    ```
5.  **Language Selection:**
    *   Upon starting, the script will first ask you to select a language. For example:
        `Select language (e.g., en, es):`
    *   Enter the language code for your preferred language (e.g., `en` for English, `es` for Spanish, `ger` for German, etc.). If an unsupported language is entered, it will default to English.

6.  **Adding Names:**
    *   After selecting the language, you will be prompted to enter names. For example (in English):
        `Enter your name (or type 'quit' to exit, 'next' to select a name):`
    *   Type a name and press Enter. The script will confirm that the name has been added.
    *   Repeat this step to add as many names as you need.

7.  **Selecting a Winner:**
    *   When you are ready to select a winner, type `next` (or the equivalent command in your selected language) and press Enter.
    *   The script will randomly choose a name from the list, announce the winner, and remove them from the selection pool.
    *   It will also inform you how many names are remaining.

8.  **Quitting the Program:**
    *   To exit the program at any time, type `quit` (or the equivalent command in your selected language) and press Enter.

9.  **Game Over:**
    *   If all names have been selected, the script will display a "Game is over!" message along with the list of all winners.

## Supported Languages

The script currently supports the following language codes for translations:

*   `en` (English)
*   `es` (Spanish)
*   `ger` (German)
*   `el` (Greek)
*   `ar` (Arabic)
*   `fi` (Finnish)
*   `sv` (Swedish)
*   `ru` (Russian)
*   `pt` (Portuguese)
*   `uk` (Ukrainian)
*   `pa` (Punjabi)
*   `gu` (Gujarati)
*   `kn` (Kannada)
*   `ml` (Malayalam)
*   `ur` (Urdu)
*   `ga` (Irish)
*   `is` (Icelandic)
*   `lv` (Latvian)
*   `sk` (Slovak)
*   `hr` (Croatian)
*   `bg` (Bulgarian)
*   `mt` (Maltese)
*   `ja` (Japanese)
*   `ko` (Korean)
*   `vi` (Vietnamese)
*   `th` (Thai)
*   `ms` (Malay)
*   `fil` (Filipino)
*   `tr` (Turkish)
*   `fa` (Persian)
*   `he` (Hebrew)
*   `zh-CN` (Simplified Chinese)
*   `zh-TW` (Traditional Chinese)

#contributors
 @yantr-manav
 
