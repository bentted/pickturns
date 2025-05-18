import random
import tkinter as tk
from tkinter import ttk

from util import translation_manager
names = []
winners = []

translations = translation_manager.get_languages("translations")

boardgames=["Monopoly", "Risk", "Settlers of Catan", "Axis & Allies", "Backgammon", "Clue", "The Game of Life", "Ludo",
            "Can't Stop", "Chicago Express", "Formula D", "Las Vegas", "Shut the Box", "Trouble", "Yahtzee", "King of Tokyo",
            "Dice Forge", "Roll for the Galaxy", "Stone Age", "Machi Koro", "Liar’s Dice", "Zombie Dice", "Qwixx", 
            "Betrayal at House on the Hill", "Descent: Legends of the Dark", "Nemesis", "Brikks", "King of the Dice", "Ruin It",
            "Wits & Wagers Deluxe", "Mahadev Jumbo Sequence", "Santa’s Rooftop Scramble", "One Night Ultimate Alien"

]
card_games_list = ["Poker", "Blackjack", "Rummy", "Bridge", "Euchre", "Hearts", "Spades", "Go Fish", "Uno", "Crazy Eights", "Pinochle", "Canasta", "Gin Rummy", "Old Maid", "War", "Solitaire", "Snap", "Cribbage", "Whist", "Durak", "President", "Exploding Kittens", "Mao", "Skat", "Baccarat", "Bezique", "Briscola", "Piquet", "Napoleon", "Patience", "Sheepshead", "Ombre", "Scopa", "Tressette", "Cuarenta", "Hanafuda", "Tarot", "Wizard", "Dutch Blitz", "Phase 10"]

card_game_rules_translations = translation_manager.get_languages("card_game_rules_translations")

current_language = "en" 

# Moved get_message function here
def get_message(key, **kwargs):
    """Retrieves a translated message string for the current language."""
    global current_language
    
    # Try current language
    lang_dict = translations.get(current_language, {}) 
    message_template = lang_dict.get(key)

    if message_template is None:
        # Try English if not found in current language or if current_language itself was not found
        lang_dict_en = translations.get("en", {})
        message_template = lang_dict_en.get(key)
    
    if message_template is None: # If key also not in English (or English dict missing), return the key itself
        return key 
    return message_template.format(**kwargs)

# ---------- Styling Constants ----------
BG_COLOR = "#f0f8ff"
PRIMARY_COLOR = "#007acc"
TEXT_COLOR = "#333333"
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_INPUT = ("Helvetica", 12)
FONT_DISPLAY = ("Helvetica", 14, "italic")

# ---------- Dice Roller Functions ----------
def roll_dice():
    """Simulates rolling two dice and updates the UI with the result and an animation."""
    selected_game = game_var.get()

    # Animation part
    animation_duration = 0.5  # seconds
    frames_per_second = 20
    num_frames = int(animation_duration * frames_per_second)
    delay_between_frames = int(1000 / frames_per_second)  # milliseconds

    def update_animation(frame_count):
        if frame_count > 0:
            # Display random numbers for animation
            anim_d1 = random.randint(1, 6)
            anim_d2 = random.randint(1, 6)
            anim_result = anim_d1 + anim_d2
            dice_result_var.set(get_message("dice_roll_result", result=anim_result, d1=anim_d1, d2=anim_d2, game=selected_game))
            root.after(delay_between_frames, lambda: update_animation(frame_count - 1))
        else:
            # Final roll
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            result = d1 + d2
            dice_result_var.set(get_message("dice_roll_result", result=result, d1=d1, d2=d2, game=selected_game))

    update_animation(num_frames)

# ---------- D&D Dice Functions ----------
def roll_dnd_die(die_type):
    """Rolls a D&D die and updates the D&D result label with an animation."""
    num_sides = int(die_type[1:]) # e.g., D20 -> 20
    
    # Animation part
    animation_duration = 0.5 # seconds
    frames_per_second = 20
    num_frames = int(animation_duration * frames_per_second)
    delay_between_frames = int(1000 / frames_per_second) # milliseconds

    def update_animation(frame_count):
        if frame_count > 0:
            # Display a random number for animation
            animated_roll = random.randint(1, num_sides)
            dnd_result_var.set(get_message("dnd_roll_result", die=die_type, result=animated_roll))
            root.after(delay_between_frames, lambda: update_animation(frame_count - 1))
        else:
            # Final roll
            roll_result = random.randint(1, num_sides)
            dnd_result_var.set(get_message("dnd_roll_result", die=die_type, result=roll_result))

    update_animation(num_frames)


def show_dnd_help():
    """Displays a pop-up window with D&D dice information."""
    help_window = tk.Toplevel(root)
    help_window.title(get_message("dnd_help_title"))
    help_window.configure(bg=BG_COLOR)
    help_window.geometry("350x450") # Adjusted size for more content

    help_text_widget = tk.Text(help_window, wrap=tk.WORD, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_INPUT, relief=tk.FLAT, spacing1=5, spacing2=5, spacing3=5)
    help_text_widget.pack(padx=10, pady=10, fill="both", expand=True)

    dice_info = [
        ("D4", get_message("d4_description")),
        ("D6", get_message("d6_description")),
        ("D8", get_message("d8_description")),
        ("D10", get_message("d10_description")),
        ("D12", get_message("d12_description")),
        ("D20", get_message("d20_description")),
        ("D100", get_message("d100_description")),
    ]

    for die, desc in dice_info:
        help_text_widget.insert(tk.END, f"{die}:\n", ("bold_underline",))
        help_text_widget.insert(tk.END, f"{desc}\n\n")

    help_text_widget.tag_configure("bold_underline", font=(FONT_INPUT[0], FONT_INPUT[1], "bold underline"))
    help_text_widget.config(state=tk.DISABLED) # Make text read-only

    close_button = ttk.Button(help_window, text=get_message("close_button_text"), command=help_window.destroy)
    close_button.pack(pady=10)

# ---------- GUI Functions -----------
def show_name_selector_frame():
    dice_roller_frame.pack_forget()
    dnd_frame.pack_forget() # Hide D&D frame
    card_game_frame.pack_forget() # Hide Card Game frame
    name_selector_frame.pack(fill="both", expand=True)
    update_ui_language() # Refresh button text

def show_dice_roller_frame():
    name_selector_frame.pack_forget()
    dnd_frame.pack_forget() # Hide D&D frame
    card_game_frame.pack_forget() # Hide Card Game frame
    dice_roller_frame.pack(fill="both", expand=True)
    update_ui_language() # Refresh button text

def show_dnd_frame():
    name_selector_frame.pack_forget()
    dice_roller_frame.pack_forget()
    card_game_frame.pack_forget() # Hide Card Game frame
    dnd_frame.pack(fill="both", expand=True)
    update_ui_language()

def show_card_game_frame(): # New function for Card Game screen
    name_selector_frame.pack_forget()
    dice_roller_frame.pack_forget()
    dnd_frame.pack_forget()
    card_game_frame.pack(fill="both", expand=True)
    update_ui_language()

def add_name_ui():
    """Handles adding a name from the UI input to the names list."""
    name = name_entry.get().strip()
    if name:
        names.append(name)
        display_var.set(get_message("name_added_to_list", name=name))
        name_entry.delete(0, tk.END)
    else:
        display_var.set(get_message("enter_name_prompt_ui"))

def select_name_ui():
    """Handles selecting a winner from the names list and displaying it."""
    if names:
        selected_winner = random.choice(names)
        names.remove(selected_winner)
        winners.append(selected_winner)
        display_var.set(get_message("congratulations_winner", name=selected_winner))

        if not names:  # All names have been picked
            # Enumerate winners in the order they were selected
            winners_text = ", ".join(f"{i+1}. {w}" for i, w in enumerate(winners))
            display_var.set(get_message("game_over_all_selected", winners_list=winners_text))
    else:
        if winners: # Game is already over, show final list again or a specific message
            winners_text = ", ".join(f"{i+1}. {w}" for i, w in enumerate(winners))
            display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\\n" + get_message("no_more_names_to_select"))
        else: # No names were ever added
            display_var.set(get_message("no_names_to_select"))

# ---------- Language Selection Functions ----------
def update_ui_language(lang_code=None):
    """Updates all UI text elements to the selected language."""
    global current_language, root, title_label, select_button, add_name_button, display_var, lang_combo_label
    global dice_roller_title_label, select_game_label, roll_dice_button
    global name_selector_to_dice_button, dice_roller_to_name_button
    global dnd_title_label, name_selector_to_dnd_button, dice_roller_to_dnd_button, dnd_to_name_selector_button, dnd_to_dice_roller_button
    global dnd_roll_d4_button, dnd_roll_d6_button, dnd_roll_d8_button, dnd_roll_d10_button, dnd_roll_d12_button, dnd_roll_d20_button, dnd_roll_d100_button, dnd_help_button
    global card_game_title_label, select_card_game_dropdown_label, card_game_rules_display_label # New label for card game screen dropdown
    global name_selector_to_card_game_button, dice_roller_to_card_game_button, dnd_to_card_game_button # New navigation buttons
    global card_game_to_name_selector_button, card_game_to_dice_roller_button, card_game_to_dnd_button # New navigation buttons

    if lang_code and lang_code in translations:
        current_language = lang_code
    
    root.title(get_message("app_title"))
    if 'lang_combo_label' in globals() and lang_combo_label:
        lang_combo_label.config(text=get_message("language_dropdown_label"))
    if 'title_label' in globals() and title_label:
        title_label.config(text=get_message("enter_name_label"))
    if 'select_button' in globals() and select_button:
        select_button.config(text=get_message("select_name_button"))
    if 'add_name_button' in globals() and add_name_button:
        add_name_button.config(text=get_message("add_name_button"))
    
    # Update dice roller UI elements
    if 'dice_roller_title_label' in globals() and dice_roller_title_label:
        dice_roller_title_label.config(text=get_message("dice_roller_title"))
    if 'select_game_label' in globals() and select_game_label:
        select_game_label.config(text=get_message("select_game_label"))
    if 'roll_dice_button' in globals() and roll_dice_button:
        roll_dice_button.config(text=get_message("roll_dice_button"))

    # Update D&D screen title
    if 'dnd_title_label' in globals() and dnd_title_label:
        dnd_title_label.config(text=get_message("dnd_screen_title"))

    # Update Card Game screen title
    if 'card_game_title_label' in globals() and card_game_title_label:
        card_game_title_label.config(text=get_message("card_game_screen_title"))
    
    # Update Card Game screen dropdown label
    if 'select_card_game_dropdown_label' in globals() and select_card_game_dropdown_label:
        select_card_game_dropdown_label.config(text=get_message("select_card_game_label"))
    
    # Update Card Game rules display label
    if 'card_game_rules_display_label' in globals() and card_game_rules_display_label:
        card_game_rules_display_label.config(text=get_message("card_game_rules_title"))
        show_card_game_rules() # Refresh rules text if a game is selected

    # Update D&D buttons
    if 'dnd_roll_d4_button' in globals() and dnd_roll_d4_button: dnd_roll_d4_button.config(text=get_message("dnd_roll_button", die="D4"))
    if 'dnd_roll_d6_button' in globals() and dnd_roll_d6_button: dnd_roll_d6_button.config(text=get_message("dnd_roll_button", die="D6"))
    if 'dnd_roll_d8_button' in globals() and dnd_roll_d8_button: dnd_roll_d8_button.config(text=get_message("dnd_roll_button", die="D8"))
    if 'dnd_roll_d10_button' in globals() and dnd_roll_d10_button: dnd_roll_d10_button.config(text=get_message("dnd_roll_button", die="D10"))
    if 'dnd_roll_d12_button' in globals() and dnd_roll_d12_button: dnd_roll_d12_button.config(text=get_message("dnd_roll_button", die="D12"))
    if 'dnd_roll_d20_button' in globals() and dnd_roll_d20_button: dnd_roll_d20_button.config(text=get_message("dnd_roll_button", die="D20"))
    if 'dnd_roll_d100_button' in globals() and dnd_roll_d100_button: dnd_roll_d100_button.config(text=get_message("dnd_roll_button", die="D100"))
    if 'dnd_help_button' in globals() and dnd_help_button: dnd_help_button.config(text=get_message("dnd_help_button"))

    # Update navigation buttons text
    if 'name_selector_to_dice_button' in globals() and name_selector_to_dice_button:
        name_selector_to_dice_button.config(text=get_message("go_to_dice_roller"))
    if 'dice_roller_to_name_button' in globals() and dice_roller_to_name_button:
        dice_roller_to_name_button.config(text=get_message("go_to_name_selector"))
    if 'name_selector_to_dnd_button' in globals() and name_selector_to_dnd_button:
        name_selector_to_dnd_button.config(text=get_message("go_to_dnd_screen"))
    if 'dice_roller_to_dnd_button' in globals() and dice_roller_to_dnd_button:
        dice_roller_to_dnd_button.config(text=get_message("go_to_dnd_screen"))
    if 'dnd_to_name_selector_button' in globals() and dnd_to_name_selector_button:
        dnd_to_name_selector_button.config(text=get_message("go_to_name_selector"))
    if 'dnd_to_dice_roller_button' in globals() and dnd_to_dice_roller_button:
        dnd_to_dice_roller_button.config(text=get_message("go_to_dice_roller"))
    
    # Update new navigation buttons for Card Game Screen
    if 'name_selector_to_card_game_button' in globals() and name_selector_to_card_game_button:
        name_selector_to_card_game_button.config(text=get_message("go_to_card_game_screen"))
    if 'dice_roller_to_card_game_button' in globals() and dice_roller_to_card_game_button:
        dice_roller_to_card_game_button.config(text=get_message("go_to_card_game_screen"))
    if 'dnd_to_card_game_button' in globals() and dnd_to_card_game_button:
        dnd_to_card_game_button.config(text=get_message("go_to_card_game_screen"))
    if 'card_game_to_name_selector_button' in globals() and card_game_to_name_selector_button:
        card_game_to_name_selector_button.config(text=get_message("go_to_name_selector"))
    if 'card_game_to_dice_roller_button' in globals() and card_game_to_dice_roller_button:
        card_game_to_dice_roller_button.config(text=get_message("go_to_dice_roller"))
    if 'card_game_to_dnd_button' in globals() and card_game_to_dnd_button:
        card_game_to_dnd_button.config(text=get_message("go_to_dnd_screen"))

    # Update status message based on current game state or set to initial
    if not names and not winners:
        display_var.set(get_message("status_initial"))
    elif not names and winners: # Game is over
        winners_text = ", ".join(f"{i+1}. {w}" for i, w in enumerate(winners))
        display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\\n" + get_message("no_more_names_to_select"))
    # else: keep current message if a name was just added or selected.

def on_language_select(event):
    """Handles the event when a new language is selected from the Combobox."""
    global language_var
    selected_lang = language_var.get()
    update_ui_language(selected_lang)
    # If game is over, re-display the game over message in new lang
    # Or if no names, display initial status
    if not names and winners: 
        winners_text = ", ".join(f"{i+1}. {w}" for i, w in enumerate(winners))
        display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\\n" + get_message("no_more_names_to_select"))
    elif not names and not winners:
        display_var.set(get_message("status_initial"))
    
    # If on card game screen, update rules display
    if card_game_frame.winfo_ismapped():
        show_card_game_rules()


# ---------- Card Game Screen Functions ----------
def show_card_game_rules(event=None):
    """Displays the rules for the selected card game."""
    global current_language # Ensure we are using the global current_language
    selected_game = card_game_var.get()
    
    # Try to get rules for the current language
    lang_rules = card_game_rules_translations.get(current_language, {})
    rules = lang_rules.get(selected_game)
    
    # If rules not found for current language, fall back to English
    if rules is None:
        lang_rules_en = card_game_rules_translations.get("en", {}) # Default to "en" if it exists
        rules = lang_rules_en.get(selected_game, "Rules not available for this game.") # Fallback message
    
    # Enable the text widget, clear it, insert new rules, then disable it
    card_game_rules_text.config(state=tk.NORMAL)
    card_game_rules_text.delete("1.0", tk.END)
    card_game_rules_text.insert(tk.END, rules)
    card_game_rules_text.config(state=tk.DISABLED)

# ---------- Main Window ----------
root = tk.Tk()
root.geometry("400x600") # Increased height for D&D screen elements
root.configure(bg=BG_COLOR)

# ---------- Frames for different screens ----------
name_selector_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
dice_roller_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
dnd_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame') # D&D Frame
card_game_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame') # Card Game Frame

style = ttk.Style()
style.configure('TFrame', background=BG_COLOR)

# ---------- Style Configuration ----------
style.theme_use("default")

style.configure('TLabel',
                background=BG_COLOR,
                foreground=TEXT_COLOR,
                font=FONT_INPUT)

style.configure('TEntry',
                font=FONT_INPUT)

style.configure('TButton',
                font=FONT_INPUT,
                foreground='white',
                background=PRIMARY_COLOR,
                padding=6)

style.map('TButton',
          background=[('active', '#005f99')])

# ---------- Widgets ----------
# --- Language Selector (Common to both frames, placed above) ---
lang_combo_label = ttk.Label(root) # Text will be set by update_ui_language
lang_combo_label.pack(pady=(10,0))

language_options = list(translations.keys())
language_var = tk.StringVar(value=current_language)
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=language_options, state="readonly", width=38)
language_dropdown.pack(pady=(0,10))
language_dropdown.bind("<<ComboboxSelected>>", on_language_select)

# --- Name Selector Frame Widgets ---
title_label = ttk.Label(name_selector_frame, font=FONT_TITLE) 
title_label.pack(pady=(5, 10))

name_entry = ttk.Entry(name_selector_frame, width=30)
name_entry.pack(pady=5)

select_button = ttk.Button(name_selector_frame, command=select_name_ui) 
select_button.pack(pady=10)

add_name_button = ttk.Button(name_selector_frame, command=add_name_ui) 
add_name_button.pack(pady=5)

display_var = tk.StringVar()
display_label = ttk.Label(name_selector_frame, textvariable=display_var, font=FONT_DISPLAY, foreground=PRIMARY_COLOR, wraplength=380)
display_label.pack(pady=(10, 10))

# Navigation buttons for Name Selector frame
name_selector_nav_frame = ttk.Frame(name_selector_frame, style='TFrame')
name_selector_nav_frame.pack(pady=(10,0), fill='x', expand=True)

name_selector_to_dice_button = ttk.Button(name_selector_nav_frame, command=show_dice_roller_frame)
name_selector_to_dice_button.pack(side=tk.LEFT, expand=True, padx=2)

name_selector_to_dnd_button = ttk.Button(name_selector_nav_frame, command=show_dnd_frame)
name_selector_to_dnd_button.pack(side=tk.LEFT, expand=True, padx=2)

name_selector_to_card_game_button = ttk.Button(name_selector_nav_frame, command=show_card_game_frame) # New Button
name_selector_to_card_game_button.pack(side=tk.LEFT, expand=True, padx=2)


# --- Dice Roller Frame Widgets ---
dice_roller_title_label = ttk.Label(dice_roller_frame, font=FONT_TITLE) 
dice_roller_title_label.pack(pady=(10,0))

select_game_label = ttk.Label(dice_roller_frame) 
select_game_label.pack(pady=(5,0))

game_var = tk.StringVar(value=boardgames[0] if boardgames else "")
game_dropdown = ttk.Combobox(dice_roller_frame, textvariable=game_var, values=boardgames, state="readonly", width=38)
game_dropdown.pack(pady=(0,5))

roll_dice_button = ttk.Button(dice_roller_frame, command=roll_dice) 
roll_dice_button.pack(pady=5)

dice_result_var = tk.StringVar()
dice_result_label = ttk.Label(dice_roller_frame, textvariable=dice_result_var, font=FONT_DISPLAY, foreground=PRIMARY_COLOR, wraplength=380)
dice_result_label.pack(pady=(5,10))

# Navigation buttons for Dice Roller frame
dice_roller_nav_frame = ttk.Frame(dice_roller_frame, style='TFrame')
dice_roller_nav_frame.pack(pady=(10,0), fill='x', expand=True)

dice_roller_to_name_button = ttk.Button(dice_roller_nav_frame, command=show_name_selector_frame)
dice_roller_to_name_button.pack(side=tk.LEFT, expand=True, padx=2)

dice_roller_to_dnd_button = ttk.Button(dice_roller_nav_frame, command=show_dnd_frame)
dice_roller_to_dnd_button.pack(side=tk.LEFT, expand=True, padx=2)

dice_roller_to_card_game_button = ttk.Button(dice_roller_nav_frame, command=show_card_game_frame) # New Button
dice_roller_to_card_game_button.pack(side=tk.LEFT, expand=True, padx=2)

# --- Dungeons & Dragons Frame Widgets ---
dnd_title_label = ttk.Label(dnd_frame, font=FONT_TITLE)
dnd_title_label.pack(pady=(10,0))

# Frame for D&D dice buttons for better layout
dnd_dice_buttons_frame = ttk.Frame(dnd_frame, style='TFrame')
dnd_dice_buttons_frame.pack(pady=(10,5))

# D&D Dice Buttons
dice_types = ["D4", "D6", "D8", "D10", "D12", "D20", "D100"]
# Store buttons in a dictionary to update their text later if needed
dnd_buttons = {}
for i, die_type in enumerate(dice_types):
    button = ttk.Button(dnd_dice_buttons_frame, text=get_message("dnd_roll_button", die=die_type), command=lambda dt=die_type: roll_dnd_die(dt))
    # Arrange in 2 columns
    button.grid(row=i // 2, column=i % 2, padx=5, pady=2, sticky="ew")
    globals()[f'dnd_roll_{die_type.lower()}_button'] = button # Make button accessible for language update

# Help Button
dnd_help_button = ttk.Button(dnd_dice_buttons_frame, text=get_message("dnd_help_button"), command=show_dnd_help)
dnd_help_button.grid(row=(len(dice_types) +1) // 2 , column=0, columnspan=2, padx=5, pady=5, sticky="ew") # Span across columns

# D&D Result Label
dnd_result_var = tk.StringVar()
dnd_result_label = ttk.Label(dnd_frame, textvariable=dnd_result_var, font=FONT_DISPLAY, foreground=PRIMARY_COLOR, wraplength=380)
dnd_result_label.pack(pady=(5,10))

# Navigation buttons for D&D frame
dnd_nav_frame = ttk.Frame(dnd_frame, style='TFrame')
dnd_nav_frame.pack(pady=(10,0), fill='x', expand=True)

dnd_to_name_selector_button = ttk.Button(dnd_nav_frame, command=show_name_selector_frame)
dnd_to_name_selector_button.pack(side=tk.LEFT, expand=True, padx=2)

dnd_to_dice_roller_button = ttk.Button(dnd_nav_frame, command=show_dice_roller_frame)
dnd_to_dice_roller_button.pack(side=tk.LEFT, expand=True, padx=2)

dnd_to_card_game_button = ttk.Button(dnd_nav_frame, command=show_card_game_frame) # New Button
dnd_to_card_game_button.pack(side=tk.LEFT, expand=True, padx=2)

# --- Card Game Frame Widgets ---
card_game_title_label = ttk.Label(card_game_frame, font=FONT_TITLE)
card_game_title_label.pack(pady=(10,0))

# Label for card game dropdown
select_card_game_dropdown_label = ttk.Label(card_game_frame)
select_card_game_dropdown_label.pack(pady=(5,0))

# Card game dropdown
card_game_var = tk.StringVar(value=card_games_list[0] if card_games_list else "")
card_game_dropdown = ttk.Combobox(card_game_frame, textvariable=card_game_var, values=card_games_list, state="readonly", width=38)
card_game_dropdown.pack(pady=(0,10))
card_game_dropdown.bind("<<ComboboxSelected>>", show_card_game_rules) # Bind event to show rules

# Label for rules display
card_game_rules_display_label = ttk.Label(card_game_frame, font=FONT_INPUT) # Will be set by update_ui_language
card_game_rules_display_label.pack(pady=(10,0))

# Text widget for displaying card game rules
card_game_rules_text = tk.Text(card_game_frame, wrap=tk.WORD, height=10, width=40, font=FONT_INPUT, relief=tk.SUNKEN, borderwidth=1)
card_game_rules_text.pack(pady=(0,10), fill="x", expand=True)
card_game_rules_text.config(state=tk.DISABLED) # Make it read-only initially


# Placeholder for card game content (e.g., buttons for draw card, shuffle, etc.)
# card_game_content_label = ttk.Label(card_game_frame, text="Card game features will be added here.", font=FONT_INPUT) # Commented out or remove if rules take its place
# card_game_content_label.pack(pady=20)

# Navigation buttons for Card Game frame
card_game_nav_frame = ttk.Frame(card_game_frame, style='TFrame')
card_game_nav_frame.pack(pady=(10,0), fill='x', expand=True)

card_game_to_name_selector_button = ttk.Button(card_game_nav_frame, command=show_name_selector_frame)
card_game_to_name_selector_button.pack(side=tk.LEFT, expand=True, padx=2)

card_game_to_dice_roller_button = ttk.Button(card_game_nav_frame, command=show_dice_roller_frame)
card_game_to_dice_roller_button.pack(side=tk.LEFT, expand=True, padx=2)

card_game_to_dnd_button = ttk.Button(card_game_nav_frame, command=show_dnd_frame)
card_game_to_dnd_button.pack(side=tk.LEFT, expand=True, padx=2)


# Initial UI language setup and frame display
show_name_selector_frame() # Show name selector by default
update_ui_language(current_language) 
if card_games_list: # If there are card games, show rules for the first one by default
    show_card_game_rules()


if __name__ == "__main__":
    # To run CLI version:
    from views import cli
    cli.set_language_cli(current_language, translations) 
    cli.main_cli(current_language, translations, winners, names)
    
    # To run GUI version:
    #root.mainloop()
