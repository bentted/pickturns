import random
import tkinter as tk
from tkinter import ttk
names = []
winners = []

translations = {
    "en": {#english translations
        "select_language_prompt": "Select language (e.g., en, es): ",
        "language_not_supported": "Language '{lang}' not supported. Using English.",
        "enter_name_prompt": "Enter your name (or type '{quit_cmd}' to exit, '{next_cmd}' to select a name): ",
        "exiting_program": "Exiting the program.",
        "no_names_to_select": "No names to select from. Please add some names first.",
        "name_added_to_list": "'{name}' added to the list.",
        "congratulations_winner": "Congratulations {name}! You are the winner!",
        "error_no_winner_provided": "Error: No winner was provided to the winner function.",
        "added_to_winners_list": "'{name}' has been added to the winners list.",
        "game_over_all_selected": "Game is over! All names have been selected. The winners are: {winners_list}",
        "names_remaining": "There are {count} names remaining in the selection pool.",
        "quit_command": "quit",
        "next_command": "next",
        # New keys for GUI
        "app_title": "Name Selector",
        "enter_name_label": "Enter a Name:",
        "select_name_button": "Select Name",
        "add_name_button": "Add Name",
        "status_initial": "Add names and click 'Select Name'.",
        "language_dropdown_label": "Language:",
        "enter_name_prompt_ui": "Please enter a name to add.",
        "dice_roller_title": "Dice Roller",
        "select_game_label": "Select Board Game:",
        "roll_dice_button": "Roll Dice",
        "dice_roll_result": "You rolled: {result} (Dice 1: {d1}, Dice 2: {d2}) for {game}",
        "go_to_dice_roller": "Go to Dice Roller",
        "go_to_name_selector": "Go to Name Selector",
        "dnd_screen_title": "Dungeons & Dragons Helper",
        "go_to_dnd_screen": "Go to D&D Helper",
        "dnd_roll_button": "Roll {die}",
        "dnd_roll_result": "You rolled a {die}: {result}",
        "dnd_help_button": "Help",
        "dnd_help_title": "Dice Information",
        "d4_description": "D4 (four-sided die) – Used for small damage rolls, such as daggers or magic missile spells.",
        "d6_description": "D6 (six-sided die) – Common for weapon damage, like short swords, and also used in character creation.",
        "d8_description": "D8 (eight-sided die) – Often used for moderate damage weapons, such as maces and certain spells.",
        "d10_description": "D10 (ten-sided die) – Used for larger damage rolls, such as certain martial weapons and spell effects.",
        "d12_description": "D12 (twelve-sided die) – Typically used for heavy weapon damage, like a barbarian’s greataxe.",
        "d20_description": "D20 (twenty-sided die) – The most important die, used for attack rolls, skill checks, saving throws, and determining success or failure.",
        "d100_description": "D100 (percentile die) – Used for rolling percentages, often in conjunction with a D10 to determine random effects or loot.",
        "no_more_names_to_select": "No more names to select.",
        "close_button_text": "Close"
    },
    "es": { #  Spanish translations
        "select_language_prompt": "Selecciona el idioma (ej. en, es): ",
        "language_not_supported": "Idioma '{lang}' no soportado. Usando Inglés.",
        "enter_name_prompt": "Introduce tu nombre (o escribe '{quit_cmd}' para salir, '{next_cmd}' para seleccionar un nombre): ",
        "exiting_program": "Saliendo del programa.",
        "no_names_to_select": "No hay nombres para seleccionar. Por favor, añade algunos nombres primero.",
        "name_added_to_list": "'{name}' añadido a la lista.",
        "congratulations_winner": "¡Felicidades {name}! ¡Eres el ganador!",
        "error_no_winner_provided": "Error: No se proporcionó ningún ganador a la función de ganador.",
        "added_to_winners_list": "'{name}' ha sido añadido a la lista de ganadores.",
        "game_over_all_selected": "¡Juego terminado! Todos los nombres han sido seleccionados. Los ganadores son: {winners_list}",
        "names_remaining": "Quedan {count} nombres en el grupo de selección.",
        "quit_command": "salir",
        "next_command": "siguiente",
        # New keys for GUI
        "app_title": "Selector de Nombres",
        "enter_name_label": "Introduce un Nombre:",
        "select_name_button": "Seleccionar Nombre",
        "add_name_button": "Añadir Nombre",
        "status_initial": "Añade nombres y haz clic en 'Seleccionar Nombre'.",
        "language_dropdown_label": "Idioma:",
        "enter_name_prompt_ui": "Por favor, introduce un nombre para añadir.",
        "dice_roller_title": "Lanzador de Dados",
        "select_game_label": "Selecciona Juego de Mesa:",
        "roll_dice_button": "Lanzar Dados",
        "dice_roll_result": "Sacaste: {result} (Dado 1: {d1}, Dado 2: {d2}) para {game}",
        "go_to_dice_roller": "Ir al Lanzador de Dados",
        "go_to_name_selector": "Ir al Selector de Nombres",
        "dnd_screen_title": "Ayudante de Dungeons & Dragons",
        "go_to_dnd_screen": "Ir al Ayudante de D&D",
        "dnd_roll_button": "Lanzar {die}",
        "dnd_roll_result": "Sacaste un {die}: {result}",
        "dnd_help_button": "Ayuda",
        "dnd_help_title": "Información de Dados",
        "d4_description": "D4 (dado de cuatro caras) – Usado para tiradas de daño pequeño, como dagas o conjuros de misiles mágicos.",
        "d6_description": "D6 (dado de seis caras) – Común para daño de armas, como espadas cortas, y también usado en la creación de personajes.",
        "d8_description": "D8 (dado de ocho caras) – A menudo usado para armas de daño moderado, como mazas y ciertos conjuros.",
        "d10_description": "D10 (dado de diez caras) – Usado para tiradas de daño mayor, como ciertas armas marciales y efectos de conjuros.",
        "d12_description": "D12 (dado de doce caras) – Típicamente usado para daño de armas pesadas, como el hacha grande de un bárbaro.",
        "d20_description": "D20 (dado de veinte caras) – El dado más importante, usado para tiradas de ataque, pruebas de habilidad, tiros de salvación y para determinar el éxito o fracaso.",
        "d100_description": "D100 (dado percentil) – Usado para tirar porcentajes, a menudo junto con un D10 para determinar efectos aleatorios o botín.",
        "no_more_names_to_select": "No quedan más nombres para seleccionar.",
        "close_button_text": "Cerrar"
    },
    "ger": { # German translations
        "select_language_prompt": "Sprache auswählen (z.B. en, es, ger): ",
        "language_not_supported": "Sprache '{lang}' nicht unterstützt. Englisch wird verwendet.",
        "enter_name_prompt": "Gib deinen Namen ein (oder tippe '{quit_cmd}' zum Beenden, '{next_cmd}' zur Auswahl eines Namens): ",
        "exiting_program": "Das Programm wird beendet.",
        "no_names_to_select": "Keine Namen zur Auswahl. Bitte füge zuerst Namen hinzu.",
        "name_added_to_list": "'{name}' wurde zur Liste hinzugefügt.",
        "congratulations_winner": "Herzlichen Glückwunsch {name}! Du bist der Gewinner!",
        "error_no_winner_provided": "Fehler: Es wurde kein Gewinner an die Gewinnerfunktion übergeben.",
        "added_to_winners_list": "'{name}' wurde zur Gewinnerliste hinzugefügt.",
        "game_over_all_selected": "Das Spiel ist vorbei! Alle Namen wurden ausgewählt. Die Gewinner sind: {winners_list}",
        "names_remaining": "Es sind {count} Namen im Auswahlpool übrig.",
        "quit_command": "beenden",
        "next_command": "weiter",
        # New keys for GUI
        "app_title": "Namenswähler",
        "enter_name_label": "Namen eingeben:",
        "select_name_button": "Namen auswählen",
        "add_name_button": "Namen hinzufügen",
        "status_initial": "Fügen Sie Namen hinzu und klicken Sie auf 'Namen auswählen'.",
        "language_dropdown_label": "Sprache:",
        "enter_name_prompt_ui": "Bitte geben Sie einen Namen ein, um ihn hinzuzufügen.",
        "dice_roller_title": "Würfelbecher",
        "select_game_label": "Brettspiel auswählen:",
        "roll_dice_button": "Würfeln",
        "dice_roll_result": "Du hast gewürfelt: {result} (Würfel 1: {d1}, Würfel 2: {d2}) für {game}",
        "go_to_dice_roller": "Zum Würfelbecher",
        "go_to_name_selector": "Zum Namenswähler",
        "dnd_screen_title": "Dungeons & Dragons Helfer",
        "go_to_dnd_screen": "Zum D&D Helfer",
        "dnd_roll_button": "{die} würfeln",
        "dnd_roll_result": "Du hast einen {die} gewürfelt: {result}",
        "dnd_help_button": "Hilfe",
        "dnd_help_title": "Würfelinformationen",
        "d4_description": "W4 (vierseitiger Würfel) – Wird für kleine Schadenswürfe verwendet, z. B. für Dolche oder magische Geschosse.",
        "d6_description": "W6 (sechsseitiger Würfel) – Üblich für Waffenschaden, wie Kurzschwerter, und wird auch bei der Charaktererstellung verwendet.",
        "d8_description": "W8 (achtseitiger Würfel) – Oft für Waffen mit mittlerem Schaden verwendet, wie Streitkolben und bestimmte Zauber.",
        "d10_description": "W10 (zehnseitiger Würfel) – Wird für größere Schadenswürfe verwendet, z. B. für bestimmte Kriegswaffen und Zaubereffekte.",
        "d12_description": "W12 (zwölfseitiger Würfel) – Wird normalerweise für schweren Waffenschaden verwendet, wie die Großaxt eines Barbaren.",
        "d20_description": "W20 (zwanzigseitiger Würfel) – Der wichtigste Würfel, wird für Angriffswürfe, Fertigkeitsproben, Rettungswürfe und zur Bestimmung von Erfolg oder Misserfolg verwendet.",
        "d100_description": "W100 (Prozentwürfel) – Wird zum Würfeln von Prozentsätzen verwendet, oft in Verbindung mit einem W10, um zufällige Effekte oder Beute zu bestimmen.",
        "no_more_names_to_select": "Keine Namen mehr zur Auswahl.",
        "close_button_text": "Schließen"
    },
    # --- European Languages ---
    "fr": { # French translations
        "select_language_prompt": "Sélectionnez la langue (par ex. en, fr) : ",
        "language_not_supported": "Langue '{lang}' non supportée. Utilisation de l'anglais.",
        "enter_name_prompt": "Entrez votre nom (ou tapez '{quit_cmd}' pour quitter, '{next_cmd}' pour sélectionner un nom) : ",
        "exiting_program": "Fermeture du programme.",
        "no_names_to_select": "Aucun nom à sélectionner. Veuillez d'abord ajouter des noms.",
        "name_added_to_list": "'{name}' ajouté à la liste.",
        "congratulations_winner": "Félicitations {name} ! Vous êtes le gagnant !",
        "error_no_winner_provided": "Erreur : Aucun gagnant n'a été fourni à la fonction gagnante.",
        "added_to_winners_list": "'{name}' a été ajouté à la liste des gagnants.",
        "game_over_all_selected": "Le jeu est terminé ! Tous les noms ont été sélectionnés. Les gagnants sont : {winners_list}",
        "names_remaining": "Il reste {count} noms dans la liste de sélection.",
        "quit_command": "quitter",
        "next_command": "suivant",
        "app_title": "Sélecteur de Noms",
        "enter_name_label": "Entrez un Nom :",
        "select_name_button": "Sélectionner un Nom",
        "add_name_button": "Ajouter un Nom",
        "status_initial": "Ajoutez des noms et cliquez sur 'Sélectionner un Nom'.",
        "language_dropdown_label": "Langue :",
        "enter_name_prompt_ui": "Veuillez entrer un nom à ajouter.",
        "dice_roller_title": "Lanceur de Dés",
        "select_game_label": "Sélectionnez un Jeu de Société :",
        "roll_dice_button": "Lancer les Dés",
        "dice_roll_result": "Vous avez obtenu : {result} (Dé 1 : {d1}, Dé 2 : {d2}) pour {game}",
        "go_to_dice_roller": "Aller au Lanceur de Dés",
        "go_to_name_selector": "Aller au Sélecteur de Noms",
        "dnd_screen_title": "Assistant Dungeons & Dragons",
        "go_to_dnd_screen": "Aller à l'Assistant D&D",
        "dnd_roll_button": "Lancer {die}",
        "dnd_roll_result": "Vous avez lancé un {die}: {result}",
        "dnd_help_button": "Aide",
        "dnd_help_title": "Informations sur les Dés",
        "d4_description": "D4 (dé à quatre faces) – Utilisé pour les petits jets de dégâts, comme les dagues ou les sorts de projectiles magiques.",
        "d6_description": "D6 (dé à six faces) – Courant pour les dégâts des armes, comme les épées courtes, et également utilisé lors de la création de personnages.",
        "d8_description": "D8 (dé à huit faces) – Souvent utilisé pour les armes à dégâts modérés, comme les masses et certains sorts.",
        "d10_description": "D10 (dé à dix faces) – Utilisé pour les jets de dégâts plus importants, comme certaines armes de guerre et effets de sorts.",
        "d12_description": "D12 (dé à douze faces) – Généralement utilisé pour les dégâts des armes lourdes, comme la hache d'armes d'un barbare.",
        "d20_description": "D20 (dé à vingt faces) – Le dé le plus important, utilisé pour les jets d'attaque, les tests de compétence, les jets de sauvegarde et pour déterminer le succès ou l'échec.",
        "d100_description": "D100 (dé de pourcentage) – Utilisé pour lancer des pourcentages, souvent en conjonction avec un D10 pour déterminer des effets aléatoires ou du butin.",
        "no_more_names_to_select": "Plus de noms à sélectionner.",
        "close_button_text": "Fermer"
    },
    "it": { # Italian translations
        "select_language_prompt": "Seleziona la lingua (es. en, it): ",
        "language_not_supported": "Lingua '{lang}' non supportata. Si utilizza l'inglese.",
        "enter_name_prompt": "Inserisci il tuo nome (o digita '{quit_cmd}' per uscire, '{next_cmd}' per selezionare un nome): ",
        "exiting_program": "Uscita dal programma.",
        "no_names_to_select": "Nessun nome da selezionare. Aggiungi prima dei nomi.",
        "name_added_to_list": "'{name}' aggiunto alla lista.",
        "congratulazioni_winner": "Congratulazioni {name}! Sei il vincitore!",
        "error_no_winner_provided": "Errore: Nessun vincitore fornito alla funzione vincitore.",
        "added_to_winners_list": "'{name}' è stato aggiunto alla lista dei vincitori.",
        "game_over_all_selected": "Gioco finito! Tutti i nomi sono stati selezionati. I vincitori sono: {winners_list}",
        "names_remaining": "Rimangono {count} nomi nel pool di selezione.",
        "quit_command": "esci",
        "next_command": "prossimo",
        "app_title": "Selettore Nomi",
        "enter_name_label": "Inserisci un Nome:",
        "select_name_button": "Seleziona Nome",
        "add_name_button": "Aggiungi Nome",
        "status_initial": "Aggiungi nomi e clicca 'Seleziona Nome'.",
        "language_dropdown_label": "Lingua:",
        "enter_name_prompt_ui": "Inserisci un nome da aggiungere.",
        "dice_roller_title": "Lancia Dadi",
        "select_game_label": "Seleziona Gioco da Tavolo:",
        "roll_dice_button": "Lancia Dadi",
        "dice_roll_result": "Hai ottenuto: {result} (Dado 1: {d1}, Dado 2: {d2}) per {game}",
        "go_to_dice_roller": "Vai al Lancia Dadi",
        "go_to_name_selector": "Vai al Selettore Nomi",
        "dnd_screen_title": "Assistente Dungeons & Dragons",
        "go_to_dnd_screen": "Vai all'Assistente D&D",
        "dnd_roll_button": "Lancia {die}",
        "dnd_roll_result": "Hai lanciato un {die}: {result}",
        "dnd_help_button": "Aiuto",
        "dnd_help_title": "Informazioni sui Dadi",
        "d4_description": "D4 (dado a quattro facce) – Usato per piccoli tiri di danno, come pugnali o incantesimi di proiettili magici.",
        "d6_description": "D6 (dado a sei facce) – Comune per il danno delle armi, come spade corte, e usato anche nella creazione del personaggio.",
        "d8_description": "D8 (dado a otto facce) – Spesso usato per armi con danno moderato, come mazze e certi incantesimi.",
        "d10_description": "D10 (dado a dieci facce) – Usato per tiri di danno maggiori, come certe armi da guerra ed effetti di incantesimi.",
        "d12_description": "D12 (dado a dodici facce) – Tipicamente usato per il danno di armi pesanti, come l'ascia bipenne di un barbaro.",
        "d20_description": "D20 (dado a venti facce) – Il dado più importante, usato per tiri di attacco, prove di abilità, tiri salvezza e per determinare successo o fallimento.",
        "d100_description": "D100 (dado percentuale) – Usato per tirare percentuali, spesso in combinazione con un D10 per determinare effetti casuali o bottino.",
        "no_more_names_to_select": "Non ci sono più nomi da selezionare.",
        "close_button_text": "Chiudi"
    },
    "pt": { # Portuguese translations
        "select_language_prompt": "Selecione o idioma (ex: en, pt): ",
        "language_not_supported": "Idioma '{lang}' não suportado. Usando Inglês.",
        "enter_name_prompt": "Digite seu nome (ou '{quit_cmd}' para sair, '{next_cmd}' para selecionar um nome): ",
        "exiting_program": "Saindo do programa.",
        "no_names_to_select": "Nenhum nome para selecionar. Adicione alguns nomes primeiro.",
        "name_added_to_list": "'{name}' adicionado à lista.",
        "congratulations_winner": "Parabéns {name}! Você é o vencedor!",
        "error_no_winner_provided": "Erro: Nenhum vencedor foi fornecido para a função de vencedor.",
        "added_to_winners_list": "'{name}' foi adicionado à lista de vencedores.",
        "game_over_all_selected": "Jogo terminado! Todos os nomes foram selecionados. Os vencedores são: {winners_list}",
        "names_remaining": "Restam {count} nomes no grupo de seleção.",
        "quit_command": "sair",
        "next_command": "próximo",
        "app_title": "Seletor de Nomes",
        "enter_name_label": "Digite um Nome:",
        "select_name_button": "Selecionar Nome",
        "add_name_button": "Adicionar Nome",
        "status_initial": "Adicione nomes e clique em 'Selecionar Nome'.",
        "language_dropdown_label": "Idioma:",
        "enter_name_prompt_ui": "Por favor, digite um nome para adicionar.",
        "dice_roller_title": "Rolador de Dados",
        "select_game_label": "Selecione o Jogo de Tabuleiro:",
        "roll_dice_button": "Rolar Dados",
        "dice_roll_result": "Você rolou: {result} (Dado 1: {d1}, Dado 2: {d2}) para {game}",
        "go_to_dice_roller": "Ir para o Rolador de Dados",
        "go_to_name_selector": "Ir para o Seletor de Nomes",
        "dnd_screen_title": "Ajudante de Dungeons & Dragons",
        "go_to_dnd_screen": "Ir para o Ajudante de D&D",
        "dnd_roll_button": "Rolar {die}",
        "dnd_roll_result": "Você rolou um {die}: {result}",
        "dnd_help_button": "Ajuda",
        "dnd_help_title": "Informações sobre Dados",
        "d4_description": "D4 (dado de quatro faces) – Usado para pequenas rolagens de dano, como adagas ou feitiços de mísseis mágicos.",
        "d6_description": "D6 (dado de seis faces) – Comum para dano de armas, como espadas curtas, e também usado na criação de personagens.",
        "d8_description": "D8 (dado de oito faces) – Frequentemente usado para armas de dano moderado, como maças e certos feitiços.",
        "d10_description": "D10 (dado de dez faces) – Usado para rolagens de dano maiores, como certas armas marciais e efeitos de feitiços.",
        "d12_description": "D12 (dado de doze faces) – Normalmente usado para dano de armas pesadas, como o machado grande de um bárbaro.",
        "d20_description": "D20 (dado de vinte faces) – O dado mais importante, usado para rolagens de ataque, testes de habilidade, salvaguardas e para determinar sucesso ou fracasso.",
        "d100_description": "D100 (dado percentual) – Usado para rolar porcentagens, frequentemente em conjunto com um D10 para determinar efeitos aleatórios ou saque.",
        "no_more_names_to_select": "Não há mais nomes para selecionar.",
        "close_button_text": "Fechar"
    },
    "nl": { # Dutch translations
        "select_language_prompt": "Selecteer taal (bijv. en, nl): ",
        "language_not_supported": "Taal '{lang}' niet ondersteund. Engels wordt gebruikt.",
        "enter_name_prompt": "Voer uw naam in (of typ '{quit_cmd}' om af te sluiten, '{next_cmd}' om een naam te selecteren): ",
        "exiting_program": "Programma afsluiten.",
        "no_names_to_select": "Geen namen om uit te kiezen. Voeg eerst namen toe.",
        "name_added_to_list": "'{name}' toegevoegd aan de lijst.",
        "congratulations_winner": "Gefeliciteerd {name}! Jij bent de winnaar!",
        "error_no_winner_provided": "Fout: Geen winnaar opgegeven aan de winnaarfunctie.",
        "added_to_winners_list": "'{name}' is toegevoegd aan de winnaarslijst.",
        "game_over_all_selected": "Spel voorbij! Alle namen zijn geselecteerd. De winnaars zijn: {winners_list}",
        "names_remaining": "Er zijn nog {count} namen over in de selectiepool.",
        "quit_command": "stoppen",
        "next_command": "volgende",
        "app_title": "Namenkiezer",
        "enter_name_label": "Voer een Naam in:",
        "select_name_button": "Selecteer Naam",
        "add_name_button": "Naam Toevoegen",
        "status_initial": "Voeg namen toe en klik op 'Selecteer Naam'.",
        "language_dropdown_label": "Taal:",
        "enter_name_prompt_ui": "Voer een naam in om toe te voegen.",
        "dice_roller_title": "Dobbelsteenwerper",
        "select_game_label": "Selecteer Bordspel:",
        "roll_dice_button": "Dobbelstenen Gooien",
        "dice_roll_result": "Je gooide: {result} (Dobbelsteen 1: {d1}, Dobbelsteen 2: {d2}) voor {game}",
        "go_to_dice_roller": "Naar Dobbelsteenwerper",
        "go_to_name_selector": "Naar Namenkiezer",
        "dnd_screen_title": "Dungeons & Dragons Hulpje",
        "go_to_dnd_screen": "Naar D&D Hulpje",
        "dnd_roll_button": "Rol {die}",
        "dnd_roll_result": "Je rolde een {die}: {result}",
        "dnd_help_button": "Help",
        "dnd_help_title": "Dobbelsteeninformatie",
        "d4_description": "D4 (vierzijdige dobbelsteen) – Gebruikt voor kleine schadeworpen, zoals dolken of magische projectielspreuken.",
        "d6_description": "D6 (zeszijdige dobbelsteen) – Gebruikelijk voor wapenschade, zoals korte zwaarden, en ook gebruikt bij het maken van personages.",
        "d8_description": "D8 (achtzijdige dobbelsteen) – Vaak gebruikt voor wapens met matige schade, zoals strijdknotsen en bepaalde spreuken.",
        "d10_description": "D10 (tienzijdige dobbelsteen) – Gebruikt voor grotere schadenswürfe, zoals bepaalde oorlogswapens en spreukeffecten.",
        "d12_description": "D12 (twaalfzijdige dobbelsteen) – Typisch gebruikt voor zware wapenschade, zoals de grote bijl van een barbaar.",
        "d20_description": "D20 (twintigzijdige dobbelsteen) – De belangrijkste dobbelsteen, gebruikt voor aanvalsworpen, vaardigheidstests, reddingsworpen en om succes of falen te bepalen.",
        "d100_description": "D100 (procentuele dobbelsteen) – Gebruikt voor het rollen van percentages, vaak in combinatie met een D10 om willekeurige effecten of buit te bepalen.",
        "no_more_names_to_select": "Geen namen meer om te selecteren.",
        "close_button_text": "Sluiten"
    },
    "pl": { # Polish translations
        "select_language_prompt": "Wybierz język (np. en, pl): ",
        "language_not_supported": "Język '{lang}' nie jest obsługiwany. Używam angielskiego.",
        "enter_name_prompt": "Wpisz swoje imię (lub wpisz '{quit_cmd}' aby wyjść, '{next_cmd}' aby wybrać imię): ",
        "exiting_program": "Zamykanie programu.",
        "no_names_to_select": "Brak imion do wyboru. Najpierw dodaj imiona.",
        "name_added_to_list": "Dodano '{name}' do listy.",
        "congratulations_winner": "Gratulacje {name}! Jesteś zwycięzcą!",
        "error_no_winner_provided": "Błąd: Nie podano zwycięzcy funkcji zwycięzcy.",
        "added_to_winners_list": "Dodano '{name}' do listy zwycięzców.",
        "game_over_all_selected": "Gra zakończona! Wszystkie imiona zostały wybrane. Zwycięzcy to: {winners_list}",
        "names_remaining": "W puli pozostało {count} imion.",
        "quit_command": "wyjdź",
        "next_command": "dalej",
        "app_title": "Selektor Imion",
        "enter_name_label": "Wpisz Imię:",
        "select_name_button": "Wybierz Imię",
        "add_name_button": "Dodaj Imię",
        "status_initial": "Dodaj imiona i kliknij 'Wybierz Imię'.",
        "language_dropdown_label": "Język:",
        "enter_name_prompt_ui": "Wpisz imię, aby dodać.",
        "dice_roller_title": "Rzut Kośćmi",
        "select_game_label": "Wybierz Grę Planszową:",
        "roll_dice_button": "Rzuć Kośćmi",
        "dice_roll_result": "Wyrzuciłeś: {result} (Kość 1: {d1}, Kość 2: {d2}) dla {game}",
        "go_to_dice_roller": "Przejdź do Rzutu Kośćmi",
        "go_to_name_selector": "Przejdź do Selektora Imion",
        "dnd_screen_title": "Pomocnik Dungeons & Dragons",
        "go_to_dnd_screen": "Przejdź do Pomocnika D&D",
        "dnd_roll_button": "Rzuć {die}",
        "dnd_roll_result": "Wyrzuciłeś {die}: {result}",
        "dnd_help_button": "Pomoc",
        "dnd_help_title": "Informacje o Kościach",
        "d4_description": "K4 (kość czworościenna) – Używana do niewielkich rzutów obrażeń, takich jak sztylety lub zaklęcia magicznych pocisków.",
        "d6_description": "K6 (kość sześcienna) – Powszechna dla obrażeń broni, takich jak krótkie miecze, a także używana podczas tworzenia postaci.",
        "d8_description": "K8 (kość ośmiościenna) – Często używana dla broni o umiarkowanych obrażeniach, takich jak buławy i niektóre zaklęcia.",
        "d10_description": "K10 (kość dziesięciościenna) – Używana do większych rzutów obrażeń, takich jak niektóre bronie wojenne i efekty zaklęć.",
        "d12_description": "K12 (kość dwunastościenna) – Zazwyczaj używana do obrażeń ciężkiej broni, takiej jak wielki topór barbarzyńcy.",
        "d20_description": "K20 (kość dwudziestościenna) – Najważniejsza kość, używana do rzutów ataku, testów umiejętności, rzutów obronnych oraz do określania sukcesu lub porażki.",
        "d100_description": "K100 (kość procentowa) – Używana do rzucania procentów, często w połączeniu z K10 do określania losowych efektów lub łupów.",
        "no_more_names_to_select": "Nie ma więcej nazw do wyboru.",
        "close_button_text": "Zamknij"
    },
    "sv": { # Swedish translations
        "select_language_prompt": "Välj språk (t.ex. en, sv): ",
        "language_not_supported": "Språk '{lang}' stöds inte. Använder engelska.",
        "enter_name_prompt": "Ange ditt namn (eller skriv '{quit_cmd}' för att avsluta, '{next_cmd}' för att välja ett namn): ",
        "exiting_program": "Avslutar programmet.",
        "no_names_to_select": "Inga namn att välja från. Lägg till namn först.",
        "name_added_to_list": "'{name}' tillagd i listan.",
        "congratulations_winner": "Grattis {name}! Du är vinnaren!",
        "error_no_winner_provided": "Fel: Ingen vinnare angavs till vinnarfunktionen.",
        "added_to_winners_list": "'{name}' har lagts till i vinnarlistan.",
        "game_over_all_selected": "Spelet är över! Alla namn har valts. Vinnarna är: {winners_list}",
        "names_remaining": "Det finns {count} namn kvar i urvalspoolen.",
        "quit_command": "avsluta",
        "next_command": "nästa",
        "app_title": "Namnväljare",
        "enter_name_label": "Ange ett Namn:",
        "select_name_button": "Välj Namn",
        "add_name_button": "Lägg till Namn",
        "status_initial": "Lägg till namn och klicka på 'Välj Namn'.",
        "language_dropdown_label": "Språk:",
        "enter_name_prompt_ui": "Ange ett namn att lägga till.",
        "dice_roller_title": "Tärningskastare",
        "select_game_label": "Välj Brädspel:",
        "roll_dice_button": "Kasta Tärning",
        "dice_roll_result": "Du slog: {result} (Tärning 1: {d1}, Tärning 2: {d2}) för {game}",
        "go_to_dice_roller": "Gå till Tärningskastare",
        "go_to_name_selector": "Gå till Namnväljare",
        "dnd_screen_title": "Dungeons & Dragons Hjälpreda",
        "go_to_dnd_screen": "Gå till D&D Hjälpreda",
        "dnd_roll_button": "Slå {die}",
        "dnd_roll_result": "Du slog en {die}: {result}",
        "dnd_help_button": "Hjälp",
        "dnd_help_title": "Tärningsinformation",
        "d4_description": "T4 (fyrsidig tärning) – Används för små skadeslag, som dolkar eller trollformler med magiska projektiler.",
        "d6_description": "T6 (sexsidig tärning) – Vanlig för vapenskada, som korta svärd, och används även vid karaktärsskapande.",
        "d8_description": "T8 (åttasidig tärning) – Används ofta för vapen med måttlig skada, som stridsklubbor och vissa trollformler.",
        "d10_description": "T10 (tiosidig tärning) – Används för större skadeslag, som vissa stridsvapen och trollformelseffekter.",
        "d12_description": "T12 (tolvsidig tärning) – Används vanligtvis för tung vapenskada, som en barbars stridsyxa.",
        "d20_description": "T20 (tjugosidig tärning) – Den viktigaste tärningen, används för attackslag, färdighetsslag, räddningsslag och för att avgöra framgång eller misslyckande.",
        "d100_description": "T100 (procenttärning) – Används för att slå procent, ofta tillsammans med en T10 för att avgöra slumpmässiga effekter eller byte.",
        "no_more_names_to_select": "Inga fler namn att välja.",
        "close_button_text": "Stäng"
    },
    "el": { # Greek translations
        "select_language_prompt": "Επιλέξτε γλώσσα (π.χ. en, el): ",
        "language_not_supported": "Η γλώσσα '{lang}' δεν υποστηρίζεται. Χρήση Αγγικών.",
        "enter_name_prompt": "Εισαγάγετε το όνομά σας (ή πληκτρολογήστε '{quit_cmd}' για έξοδο, '{next_cmd}' για επιλογή ονόματος): ",
        "exiting_program": "Έξοδος από το πρόγραμμα.",
        "no_names_to_select": "Δεν υπάρχουν ονόματα προς επιλογή. Προσθέστε πρώτα ονόματα.",
        "name_added_to_list": "Το '{name}' προστέθηκε στη λίστα.",
        "congratulations_winner": "Συγχαρητήρια {name}! Είσαι ο νικητής!",
        "error_no_winner_provided": "Σφάλμα: Δεν δόθηκε νικητής στη συνάρτηση νικητή.",
        "added_to_winners_list": "Το '{name}' προστέθηκε στη λίστα νικητών.",
        "game_over_all_selected": "Το παιχνίδι τελείωσε! Όλα τα ονόματα έχουν επιλεγεί. Οι νικητές είναι: {winners_list}",
        "names_remaining": "Απομένουν {count} ονόματα στην ομάδα επιλογής.",
        "quit_command": "έξοδος",
        "next_command": "επόμενο",
        "app_title": "Επιλογέας Ονομάτων",
        "enter_name_label": "Εισαγάγετε Όνομα:",
        "select_name_button": "Επιλογή Ονόματος",
        "add_name_button": "Προσθήκη Ονόματος",
        "status_initial": "Προσθέστε ονόματα και κάντε κλικ στο 'Επιλογή Ονόματος'.",
        "language_dropdown_label": "Γλώσσα:",
        "enter_name_prompt_ui": "Παρακαλώ εισαγάγετε ένα όνομα για προσθήκη.",
        "dice_roller_title": "Ρίψη Ζαριών",
        "select_game_label": "Επιλογή Επιτραπέζιου Παιχνιδιού:",
        "roll_dice_button": "Ρίψη Ζαριών",
        "dice_roll_result": "Έριξες: {result} (Ζάρι 1: {d1}, Ζάρι 2: {d2}) για {game}",
        "go_to_dice_roller": "Μετάβαση στη Ρίψη Ζαριών",
        "go_to_name_selector": "Μετάβαση στον Επιλογέα Ονομάτων",
        "dnd_screen_title": "Βοηθός Dungeons & Dragons",
        "go_to_dnd_screen": "Μετάβαση στον Βοηθό D&D",
        "dnd_roll_button": "Ρίξε {die}",
        "dnd_roll_result": "Έριξες ένα {die}: {result}",
        "dnd_help_button": "Βοήθεια",
        "dnd_help_title": "Πληροφορίες Ζαριών",
        "d4_description": "D4 (τετράεδρο ζάρι) – Χρησιμοποιείται για μικρές ζημιές, όπως στιλέτα ή ξόρκια μαγικών βλημάτων.",
        "d6_description": "D6 (εξάεδρο ζάρι) – Συνηθισμένο για ζημιές όπλων, όπως κοντά σπαθιά, και χρησιμοποιείται επίσης στη δημιουργία χαρακτήρων.",
        "d8_description": "D8 (οκτάεδρο ζάρι) – Συχνά χρησιμοποιείται για όπλα μέτριας ζημιάς, όπως ρόπαλα και ορισμένα ξόρκια.",
        "d10_description": "D10 (δεκάεδρο ζάρι) – Χρησιμοποιείται για μεγαλύτερες ζημιές, όπως ορισμένα πολεμικά όπλα και εφέ ξορκιών.",
        "d12_description": "D12 (δωδεκάεδρο ζάρι) – Συνήθως χρησιμοποιείται για ζημιές βαρέων όπλων, όπως ο μεγάλος πέλεκυς ενός βάρβαρου.",
        "d20_description": "D20 (εικοσάεδρο ζάρι) – Το πιο σημαντικό ζάρι, χρησιμοποιείται για επιθέσεις, ελέγχους δεξιοτήτων, ρίψεις σωτηρίας και για τον καθορισμό επιτυχίας ή αποτυχίας.",
        "d100_description": "D100 (εκατοστιαίο ζάρι) – Χρησιμοποιείται για ρίψη ποσοστών, συχνά σε συνδυασμό με ένα D10 για τον καθορισμό τυχαίων εφέ ή λαφύρων.",
        "no_more_names_to_select": "Δεν υπάρχουν άλλα ονόματα για επιλογή.",
        "close_button_text": "Κλείσιμο"
    },
    "ru": { # Russian translations
        "select_language_prompt": "Выберите язык (например, en, ru): ",
        "language_not_supported": "Язык '{lang}' не поддерживается. Используется английский.",
        "enter_name_prompt": "Введите ваше имя (или введите '{quit_cmd}' для выхода, '{next_cmd}' для выбора имени): ",
        "exiting_program": "Выход из программы.",
        "no_names_to_select": "Нет имен для выбора. Пожалуйста, сначала добавьте имена.",
        "name_added_to_list": "'{name}' добавлено в список.",
        "congratulations_winner": "Поздравляем {name}! Вы победитель!",
        "error_no_winner_provided": "Ошибка: Победитель не был предоставлен функции победителя.",
        "added_to_winners_list": "'{name}' добавлено в список победителей.",
        "game_over_all_selected": "Игра окончена! Все имена выбраны. Победители: {winners_list}",
        "names_remaining": "Осталось {count} имен в пуле выбора.",
        "quit_command": "выход",
        "next_command": "далее",
        "app_title": "Выбор Имени",
        "enter_name_label": "Введите Имя:",
        "select_name_button": "Выбрать Имя",
        "add_name_button": "Добавить Имя",
        "status_initial": "Добавьте имена и нажмите 'Выбрать Имя'.",
        "language_dropdown_label": "Язык:",
        "enter_name_prompt_ui": "Пожалуйста, введите имя для добавления.",
        "dice_roller_title": "Бросок кубиков",
        "select_game_label": "Выберите настольную игру:",
        "roll_dice_button": "Бросить кубики",
        "dice_roll_result": "Вы выбросили: {result} (Кубик 1: {d1}, Кубик 2: {d2}) для {game}",
        "go_to_dice_roller": "К броску кубиков",
        "go_to_name_selector": "К выбору имени",
        "dnd_screen_title": "Помощник Dungeons & Dragons",
        "go_to_dnd_screen": "К Помощнику D&D",
        "dnd_roll_button": "Бросить {die}",
        "dnd_roll_result": "Вы бросили {die}: {result}",
        "dnd_help_button": "Помощь",
        "dnd_help_title": "Информация о кубиках",
        "d4_description": "D4 (четырехгранный кубик) – Используется для небольшого урона, например, от кинжалов или заклинаний магической стрелы.",
        "d6_description": "D6 (шестигранный кубик) – Распространен для урона от оружия, такого как короткие мечи, а также используется при создании персонажа.",
        "d8_description": "D8 (восьмигранный кубик) – Часто используется для оружия со средним уроном, такого как булавы и определенные заклинания.",
        "d10_description": "D10 (десятигранный кубик) – Используется для большего урона, например, от определенного боевого оружия и эффектов заклинаний.",
        "d12_description": "D12 (двенадцатигранный кубик) – Обычно используется для урона от тяжелого оружия, такого как двуручный топор варвара.",
        "d20_description": "D20 (двадцатигранный кубик) – Самый важный кубик, используется для бросков атаки, проверок навыков, спасбросков и определения успеха или неудачи.",
        "d100_description": "D100 (процентный кубик) – Используется для броска процентов, часто вместе с D10 для определения случайных эффектов или добычи.",
        "no_more_names_to_select": "Больше нет имен для выбора.",
        "close_button_text": "Закрыть"
    },
    # --- Asian Languages ---
    "ja": { # Japanese translations
        "select_language_prompt": "言語を選択してください (例: en, ja): ",
        "language_not_supported": "言語 '{lang}' はサポートされていません。英語を使用します。",
        "enter_name_prompt": "名前を入力してください (終了するには '{quit_cmd}'、名前を選択するには '{next_cmd}' と入力): ",
        "exiting_program": "プログラムを終了しています。",
        "no_names_to_select": "選択する名前がありません。まず名前を追加してください。",
        "name_added_to_list": "'{name}' をリストに追加しました。",
        "congratulations_winner": "おめでとうございます {name} さん！あなたが勝者です！",
        "error_no_winner_provided": "エラー: 勝者関数に勝者が提供されませんでした。",
        "added_to_winners_list": "'{name}' さんを勝者リストに追加しました。",
        "game_over_all_selected": "ゲーム終了！すべての名前が選択されました。勝者は次のとおりです: {winners_list}",
        "names_remaining": "選択プールには残り {count} 件の名前があります。",
        "quit_command": "終了",
        "next_command": "次へ",
        "app_title": "名前セレクター",
        "enter_name_label": "名前を入力:",
        "select_name_button": "名前を選択",
        "add_name_button": "名前を追加",
        "status_initial": "名前を追加して「名前を選択」をクリックしてください。",
        "language_dropdown_label": "言語:",
        "enter_name_prompt_ui": "追加する名前を入力してください。",
        "dice_roller_title": "サイコロローラー",
        "select_game_label": "ボードゲームを選択:",
        "roll_dice_button": "サイコロを振る",
        "dice_roll_result": "出目: {result} (サイコロ1: {d1}, サイコロ2: {d2}) ゲーム: {game}",
        "go_to_dice_roller": "サイコロローラーへ",
        "go_to_name_selector": "名前セレクターへ",
        "dnd_screen_title": "ダンジョンズ＆ドラゴンズ ヘルパー",
        "go_to_dnd_screen": "D&Dヘルパーへ",
        "dnd_roll_button": "{die}を振る",
        "dnd_roll_result": "{die}を振って{result}が出ました",
        "dnd_help_button": "ヘルプ",
        "dnd_help_title": "ダイス情報",
        "d4_description": "D4 (4面ダイス) – ダガーやマジックミサイル呪文など、小さなダメージロールに使用されます。",
        "d6_description": "D6 (6面ダイス) – ショートソードなどの武器ダメージに一般的で、キャラクター作成にも使用されます。",
        "d8_description": "D8 (8面ダイス) – メイスや特定の呪文など、中程度のダメージの武器によく使用されます。",
        "d10_description": "D10 (10面ダイス) – 特定の武具や呪文効果など、より大きなダメージロールに使用されます。",
        "d12_description": "D12 (12面ダイス) – バーバリアンのグレートアックスなど、重武器のダメージに通常使用されます。",
        "d20_description": "D20 (20面ダイス) – 最も重要なダイスで、攻撃ロール、技能チェック、セーヴィングスロー、成功または失敗の判定に使用されます。",
        "d100_description": "D100 (パーセンタイルダイス) – パーセンテージを振るために使用され、ランダムな効果や戦利品を決定するためにD10と組み合わせて使用されることがよくあります。",
        "no_more_names_to_select": "選択する名前はもうありません。",
        "close_button_text": "閉じる"
    },
    "ko": { # Korean translations
        "select_language_prompt": "언어를 선택하세요 (예: en, ko): ",
        "language_not_supported": "언어 '{lang}'는 지원되지 않습니다. 영어를 사용합니다.",
        "enter_name_prompt": "이름을 입력하세요 (종료하려면 '{quit_cmd}', 이름을 선택하려면 '{next_cmd}' 입력): ",
        "exiting_program": "프로그램을 종료합니다.",
        "no_names_to_select": "선택할 이름이 없습니다. 먼저 이름을 추가하세요.",
        "name_added_to_list": "'{name}'이(가) 목록에 추가되었습니다.",
        "congratulations_winner": "축하합니다 {name}님! 당신이 승자입니다!",
        "error_no_winner_provided": "오류: 승자 함수에 승자가 제공되지 않았습니다.",
        "added_to_winners_list": "'{name}'이(가) 승자 목록에 추가되었습니다.",
        "game_over_all_selected": "게임 종료! 모든 이름이 선택되었습니다. 승자는 다음과 같습니다: {winners_list}",
        "names_remaining": "선택 풀에 {count}개의 이름이 남아 있습니다.",
        "quit_command": "종료",
        "next_command": "다음",
        "app_title": "이름 선택기",
        "enter_name_label": "이름 입력:",
        "select_name_button": "이름 선택",
        "add_name_button": "이름 추가",
        "status_initial": "이름을 추가하고 '이름 선택'을 클릭하세요.",
        "language_dropdown_label": "언어:",
        "enter_name_prompt_ui": "추가할 이름을 입력하세요.",
        "dice_roller_title": "주사위 굴리개",
        "select_game_label": "보드 게임 선택:",
        "roll_dice_button": "주사위 굴리기",
        "dice_roll_result": "결과: {result} (주사위 1: {d1}, 주사위 2: {d2}) 게임: {game}",
        "go_to_dice_roller": "주사위 굴리개로 이동",
        "go_to_name_selector": "이름 선택기로 이동",
        "dnd_screen_title": "던전 앤 드래곤 헬퍼",
        "go_to_dnd_screen": "D&D 헬퍼로 이동",
        "dnd_roll_button": "{die} 굴리기",
        "dnd_roll_result": "{die}을(를) 굴려 {result}이(가) 나왔습니다",
        "dnd_help_button": "도움말",
        "dnd_help_title": "주사위 정보",
        "d4_description": "D4 (4면체 주사위) – 단검이나 매직 미사일 주문과 같은 작은 피해 굴림에 사용됩니다.",
        "d6_description": "D6 (6면체 주사위) – 짧은 검과 같은 무기 피해에 일반적이며 캐릭터 생성에도 사용됩니다.",
        "d8_description": "D8 (8면체 주사위) – 철퇴 및 특정 주문과 같은 중간 정도의 피해를 주는 무기에 자주 사용됩니다.",
        "d10_description": "D10 (10면체 주사위) – 특정 군용 무기 및 주문 효과와 같은 더 큰 피해 굴림에 사용됩니다.",
        "d12_description": "D12 (12면체 주사위) – 일반적으로 야만용사의 대형 도끼와 같은 중화기 피해에 사용됩니다.",
        "d20_description": "D20 (20면체 주사위) – 가장 중요한 주사위로 공격 굴림, 기술 확인, 내성 굴림, 성공 또는 실패 판별에 사용됩니다.",
        "d100_description": "D100 (백분위 주사위) – 백분율을 굴리는 데 사용되며 무작위 효과나 전리품을 결정하기 위해 D10과 함께 자주 사용됩니다.",
        "no_more_names_to_select": "더 이상 선택할 이름이 없습니다.",
        "close_button_text": "닫기"
    },
    "hi": { # Hindi translations
        "select_language_prompt": "भाषा चुनें (उदा. en, hi): ",
        "language_not_supported": "भाषा '{lang}' समर्थित नहीं है। अंग्रेजी का उपयोग किया जा रहा है।",
        "enter_name_prompt": "अपना नाम दर्ज करें (या बाहर निकलने के लिए '{quit_cmd}' टाइप करें, नाम चुनने के लिए '{next_cmd}' टाइप करें): ",
        "exiting_program": "कार्यक्रम से बाहर निकल रहा है।",
        "no_names_to_select": "चुनने के लिए कोई नाम नहीं है। कृपया पहले कुछ नाम जोड़ें।",
        "name_added_to_list": "'{name}' सूची में जोड़ा गया।",
        "congratulations_winner": "बधाई हो {name}! आप विजेता हैं!",
        "error_no_winner_provided": "त्रुटि: विजेता फ़ंक्शन को कोई विजेता प्रदान नहीं किया गया था।",
        "added_to_winners_list": "'{name}' को विजेताओं की सूची में जोड़ा गया है।",
        "game_over_all_selected": "खेल समाप्त! सभी नामों का चयन कर लिया गया है। विजेता हैं: {winners_list}",
        "names_remaining": "चयन पूल में {count} नाम शेष हैं।",
        "quit_command": "छोड़ें",
        "next_command": "अगला",
        "app_title": "नाम चयनकर्ता",
        "enter_name_label": "नाम दर्ज करें:",
        "select_name_button": "नाम चुनें",
        "add_name_button": "नाम जोड़ें",
        "status_initial": "नाम जोड़ें और 'नाम चुनें' पर क्लिक करें।",
        "language_dropdown_label": "भाषा:",
        "enter_name_prompt_ui": "कृपया जोड़ने के लिए एक नाम दर्ज करें।",
        "dice_roller_title": "पासा रोलर",
        "select_game_label": "बोर्ड गेम चुनें:",
        "roll_dice_button": "पासा रोल करें",
        "dice_roll_result": "आपने रोल किया: {result} (पासा 1: {d1}, पासा 2: {d2}) {game} के लिए",
        "go_to_dice_roller": "पासा रोलर पर जाएं",
        "go_to_name_selector": "नाम चयनकर्ता पर जाएं",
        "dnd_screen_title": "डंगऑन और ड्रेगन हेल्पर",
        "go_to_dnd_screen": "डी एंड डी हेल्पर पर जाएं",
        "dnd_roll_button": "रोल करें {die}",
        "dnd_roll_result": "आपने {die} रोल किया: {result}",
        "dnd_help_button": "मदद",
        "dnd_help_title": "पासा जानकारी",
        "d4_description": "D4 (चार-पक्षीय पासा) – छोटे नुकसान रोल के लिए उपयोग किया जाता है, जैसे कि खंजर या जादू मिसाइल मंत्र।",
        "d6_description": "D6 (छह-पक्षीय पासा) – हथियार के नुकसान के लिए आम, जैसे छोटी तलवारें, और चरित्र निर्माण में भी उपयोग किया जाता है।",
        "d8_description": "D8 (आठ-पक्षीय पासा) – अक्सर मध्यम क्षति वाले हथियारों के लिए उपयोग किया जाता है, जैसे गदा और कुछ मंत्र।",
        "d10_description": "D10 (दस-पक्षीय पासा) – बड़े नुकसान रोल के लिए उपयोग किया जाता है, जैसे कुछ मार्शल हथियार और जादू प्रभाव।",
        "d12_description": "D12 (बारह-पक्षीय पासा) – आमतौर पर भारी हथियार क्षति के लिए उपयोग किया जाता है, जैसे एक बर्बर का बड़ा कुल्हाड़ा।",
        "d20_description": "D20 (बीस-पक्षीय पासा) – सबसे महत्वपूर्ण पासा, हमले के रोल, कौशल जांच, बचत थ्रो और सफलता या विफलता का निर्धारण करने के लिए उपयोग किया जाता है।",
        "d100_description": "D100 (प्रतिशत पासा) – प्रतिशत रोल करने के लिए उपयोग किया जाता है, अक्सर यादृच्छिक प्रभाव या लूट का निर्धारण करने के लिए D10 के साथ संयोजन में।",
        "no_more_names_to_select": "चुनने के लिए और नाम नहीं हैं।",
        "close_button_text": "बंद करें"
    },
    "ar": { # Arabic translations
        "select_language_prompt": "اختر اللغة (مثال: en, ar): ",
        "language_not_supported": "اللغة '{lang}' غير مدعومة. يتم استخدام الإنجليزية.",
        "enter_name_prompt": "أدخل اسمك (أو اكتب '{quit_cmd}' للخروج، '{next_cmd}' لاختيار اسم): ",
        "exiting_program": "الخروج من البرنامج.",
        "no_names_to_select": "لا توجد أسماء للاختيار من بينها. الرجاء إضافة بعض الأسماء أولاً.",
        "name_added_to_list": "تمت إضافة '{name}' إلى القائمة.",
        "congratulations_winner": "تهانينا {name}! أنت الفائز!",
        "error_no_winner_provided": "خطأ: لم يتم توفير فائز لدالة الفائز.",
        "added_to_winners_list": "تمت إضافة '{name}' إلى قائمة الفائزين.",
        "game_over_all_selected": "انتهت اللعبة! تم اختيار جميع الأسماء. الفائزون هم: {winners_list}",
        "names_remaining": "يوجد {count} أسماء متبقية في مجموعة الاختيار.",
        "quit_command": "خروج",
        "next_command": "التالي",
        "app_title": "محدد الأسماء",
        "enter_name_label": "أدخل اسمًا:",
        "select_name_button": "اختر اسمًا",
        "add_name_button": "أضف اسمًا",
        "status_initial": "أضف أسماء وانقر على 'اختر اسمًا'.",
        "language_dropdown_label": "اللغة:",
        "enter_name_prompt_ui": "الرجاء إدخال اسم لإضافته.",
        "dice_roller_title": "رامي النرد",
        "select_game_label": "اختر لعبة لوحية:",
        "roll_dice_button": "ارم النرد",
        "dice_roll_result": "لقد رميت: {result} (النرد 1: {d1}, النرد 2: {d2}) للعبة {game}",
        "go_to_dice_roller": "اذهب إلى رامي النرد",
        "go_to_name_selector": "اذهب إلى محدد الأسماء",
        "dnd_screen_title": "مساعد Dungeons & Dragons",
        "go_to_dnd_screen": "اذهب إلى مساعد D&D",
        "dnd_roll_button": "ارم {die}",
        "dnd_roll_result": "لقد رميت {die}: {result}",
        "dnd_help_button": "مساعدة",
        "dnd_help_title": "معلومات النرد",
        "d4_description": "D4 (نرد رباعي الأوجه) – يستخدم لرميات الضرر الصغيرة، مثل الخناجر أو تعويذات الصواريخ السحرية.",
        "d6_description": "D6 (نرد سداسي الأوجه) – شائع لضرر الأسلحة، مثل السيوف القصيرة، ويستخدم أيضًا في إنشاء الشخصيات.",
        "d8_description": "D8 (نرد ثماني الأوجه) – غالبًا ما يستخدم لأسلحة الضرر المعتدل، مثل الصولجانات وبعض التعويذات.",
        "d10_description": "D10 (نرد عشاري الأوجه) – يستخدم لرميات الضرر الأكبر، مثل بعض أسلحة القتال وتأثيرات التعويذات.",
        "d12_description": "D12 (نرد اثني عشر الأوجه) – يستخدم عادةً لضرر الأسلحة الثقيلة، مثل فأس البربري الكبير.",
        "d20_description": "D20 (نرد عشروني الأوجه) – أهم نرد، يستخدم لرميات الهجوم، وفحوصات المهارة، ورميات الإنقاذ، وتحديد النجاح أو الفشل.",
        "d100_description": "D100 (نرد النسبة المئوية) – يستخدم لرمي النسب المئوية، غالبًا بالاقتران مع D10 لتحديد التأثيرات العشوائية أو الغنائم.",
        "no_more_names_to_select": "لا توجد أسماء أخرى للاختيار.",
        "close_button_text": "إغلاق"
    },
    "tr": { # Turkish translations
        "select_language_prompt": "Dil seçin (örn. en, tr): ",
        "language_not_supported": "Dil '{lang}' desteklenmiyor. İngilizce kullanılıyor.",
        "enter_name_prompt": "Adınızı girin (veya çıkmak için '{quit_cmd}', ad seçmek için '{next_cmd}' yazın): ",
        "exiting_program": "Programdan çıkılıyor.",
        "no_names_to_select": "Seçilecek ad yok. Lütfen önce bazı adlar ekleyin.",
        "name_added_to_list": "'{name}' listeye eklendi.",
        "congratulations_winner": "Tebrikler {name}! Kazanan sizsiniz!",
        "error_no_winner_provided": "Hata: Kazanan işlevine kazanan sağlanmadı.",
        "added_to_winners_list": "'{name}' kazananlar listesine eklendi.",
        "game_over_all_selected": "Oyun bitti! Tüm adlar seçildi. Kazananlar: {winners_list}",
        "names_remaining": "Seçim havuzunda {count} ad kaldı.",
        "quit_command": "çık",
        "next_command": "sonraki",
        "app_title": "İsim Seçici",
        "enter_name_label": "Bir İsim Girin:",
        "select_name_button": "İsim Seç",
        "add_name_button": "İsim Ekle",
        "status_initial": "İsim ekleyin ve 'İsim Seç'e tıklayın.",
        "language_dropdown_label": "Dil:",
        "enter_name_prompt_ui": "Lütfen eklenecek bir isim girin.",
        "dice_roller_title": "Zar Atıcı",
        "select_game_label": "Masa Oyunu Seçin:",
        "roll_dice_button": "Zar At",
        "dice_roll_result": "Attığınız zar: {result} (Zar 1: {d1}, Zar 2: {d2}) oyun: {game}",
        "go_to_dice_roller": "Zar Atıcıya Git",
        "go_to_name_selector": "İsim Seçiciye Git",
        "dnd_screen_title": "Dungeons & Dragons Yardımcısı",
        "go_to_dnd_screen": "D&D Yardımcısına Git",
        "dnd_roll_button": "At {die}",
        "dnd_roll_result": "Attığınız {die}: {result}",
        "dnd_help_button": "Yardım",
        "dnd_help_title": "Zar Bilgisi",
        "d4_description": "D4 (dört yüzlü zar) – Hançerler veya sihirli füze büyüleri gibi küçük hasar atışları için kullanılır.",
        "d6_description": "D6 (altı yüzlü zar) – Kısa kılıçlar gibi silah hasarı için yaygındır ve karakter oluşturmada da kullanılır.",
        "d8_description": "D8 (sekiz yüzlü zar) – Genellikle topuzlar ve belirli büyüler gibi orta derecede hasar atışları için kullanılır.",
        "d10_description": "D10 (on yüzlü zar) – Belirli dövüş silahları ve büyü etkileri gibi daha büyük hasar atışları için kullanılır.",
        "d12_description": "D12 (on iki yüzlü zar) – Genellikle bir barbarın baltası gibi ağır silah hasarı için kullanılır.",
        "d20_description": "D20 (yirmi yüzlü zar) – En önemli zar, saldırı atışları, beceri kontrolleri, kurtulma atışları ve başarı veya başarısızlığı belirlemek için kullanılır.",
        "d100_description": "D100 (yüzdelik zar) – Yüzdeleri atmak için kullanılır, genellikle rastgele etkileri veya ganimeti belirlemek için bir D10 ile birlikte kullanılır.",
        "no_more_names_to_select": "Seçilecek başka isim kalmadı.",
        "close_button_text": "Kapat"
    },
    "vi": { # Vietnamese translations
        "select_language_prompt": "Chọn ngôn ngữ (ví dụ: en, vi): ",
        "language_not_supported": "Ngôn ngữ '{lang}' không được hỗ trợ. Sử dụng tiếng Anh.",
        "enter_name_prompt": "Nhập tên của bạn (hoặc gõ '{quit_cmd}' để thoát, '{next_cmd}' để chọn tên): ",
        "exiting_program": "Đang thoát chương trình.",
        "no_names_to_select": "Không có tên để chọn. Vui lòng thêm một số tên trước.",
        "name_added_to_list": "Đã thêm '{name}' vào danh sách.",
        "congratulations_winner": "Chúc mừng {name}! Bạn là người chiến thắng!",
        "error_no_winner_provided": "Lỗi: Không có người chiến thắng nào được cung cấp cho hàm chiến thắng.",
        "added_to_winners_list": "Đã thêm '{name}' vào danh sách những người chiến thắng.",
        "game_over_all_selected": "Trò chơi kết thúc! Tất cả các tên đã được chọn. Những người chiến thắng là: {winners_list}",
        "names_remaining": "Còn lại {count} tên trong nhóm lựa chọn.",
        "quit_command": "thoát",
        "next_command": "tiếp",
        "app_title": "Bộ chọn tên",
        "enter_name_label": "Nhập tên:",
        "select_name_button": "Chọn tên",
        "add_name_button": "Thêm tên",
        "status_initial": "Thêm tên và nhấp vào 'Chọn tên'.",
        "language_dropdown_label": "Ngôn ngữ:",
        "enter_name_prompt_ui": "Vui lòng nhập tên để thêm.",
        "dice_roller_title": "Trình lăn xúc xắc",
        "select_game_label": "Chọn trò chơi board game:",
        "roll_dice_button": "Lăn xúc xắc",
        "dice_roll_result": "Bạn đã lăn: {result} (Xúc xắc 1: {d1}, Xúc xắc 2: {d2}) cho {game}",
        "go_to_dice_roller": "Đến Trình lăn xúc xắc",
        "go_to_name_selector": "Đến Bộ chọn tên",
        "dnd_screen_title": "Trợ giúp Dungeons & Dragons",
        "go_to_dnd_screen": "Đến Trợ giúp D&D",
        "dnd_roll_button": "Lăn {die}",
        "dnd_roll_result": "Bạn đã lăn {die}: {result}",
        "dnd_help_button": "Trợ giúp",
        "dnd_help_title": "Thông tin Xúc xắc",
        "d4_description": "D4 (xúc xắc bốn mặt) – Dùng cho các lần tung sát thương nhỏ, chẳng hạn như dao găm hoặc phép thuật tên lửa ma thuật.",
        "d6_description": "D6 (xúc xắc sáu mặt) – Phổ biến cho sát thương vũ khí, như kiếm ngắn, và cũng được sử dụng trong việc tạo nhân vật.",
        "d8_description": "D8 (xúc xắc tám mặt) – Thường được sử dụng cho các vũ khí sát thương vừa phải, chẳng hạn như chùy và một số phép thuật nhất định.",
        "d10_description": "D10 (xúc xắc mười mặt) – Dùng cho các lần tung sát thương lớn hơn, chẳng hạn như một số vũ khí cận chiến và hiệu ứng phép thuật.",
        "d12_description": "D12 (xúc xắc mười hai mặt) – Thường được sử dụng cho sát thương vũ khí hạng nặng, như rìu lớn của một chiến binh man rợ.",
        "d20_description": "D20 (xúc xắc hai mươi mặt) – Xúc xắc quan trọng nhất, được sử dụng cho các lần tung tấn công, kiểm tra kỹ năng, tung cứu thua và xác định thành công hay thất bại.",
        "d100_description": "D100 (xúc xắc phần trăm) – Dùng để tung phần trăm, thường kết hợp với D10 để xác định các hiệu ứng ngẫu nhiên hoặc chiến lợi phẩm.",
        "no_more_names_to_select": "Không còn tên nào để chọn.",
        "close_button_text": "Đóng"
    },
    "th": { # Thai translations
        "select_language_prompt": "เลือกภาษา (เช่น en, th): ",
        "language_not_supported": "ไม่รองรับภาษา '{lang}' กำลังใช้ภาษาอังกฤษ",
        "enter_name_prompt": "ป้อนชื่อของคุณ (หรือพิมพ์ '{quit_cmd}' เพื่อออก, '{next_cmd}' เพื่อเลือกชื่อ): ",
        "exiting_program": "กำลังออกจากโปรแกรม",
        "no_names_to_select": "ไม่มีชื่อให้เลือก โปรดเพิ่มชื่อก่อน",
        "name_added_to_list": "เพิ่ม '{name}' ในรายการแล้ว",
        "congratulations_winner": "ยินดีด้วย {name}! คุณคือผู้ชนะ!",
        "error_no_winner_provided": "ข้อผิดพลาด: ไม่มีการระบุผู้ชนะให้กับฟังก์ชันผู้ชนะ",
        "added_to_winners_list": "เพิ่ม '{name}' ในรายชื่อผู้ชนะแล้ว",
        "game_over_all_selected": "เกมจบแล้ว! เลือกชื่อทั้งหมดแล้ว ผู้ชนะคือ: {winners_list}",
        "names_remaining": "มีชื่อเหลืออยู่ {count} ชื่อในกลุ่มการเลือก",
        "quit_command": "ออก",
        "next_command": "ถัดไป",
        "app_title": "เครื่องมือเลือกชื่อ",
        "enter_name_label": "ป้อนชื่อ:",
        "select_name_button": "เลือกชื่อ",
        "add_name_button": "เพิ่มชื่อ",
        "status_initial": "เพิ่มชื่อแล้วคลิก 'เลือกชื่อ'",
        "language_dropdown_label": "ภาษา:",
        "enter_name_prompt_ui": "โปรดป้อนชื่อที่จะเพิ่ม",
        "dice_roller_title": "ลูกเต๋า",
        "select_game_label": "เลือกเกมกระดาน:",
        "roll_dice_button": "ทอยลูกเต๋า",
        "dice_roll_result": "คุณทอยได้: {result} (ลูกเต๋า 1: {d1}, ลูกเต๋า 2: {d2}) สำหรับเกม {game}",
        "go_to_dice_roller": "ไปที่ลูกเต๋า",
        "go_to_name_selector": "ไปที่เครื่องมือเลือกชื่อ",
        "dnd_screen_title": "ตัวช่วย Dungeons & Dragons",
        "go_to_dnd_screen": "ไปที่ตัวช่วย D&D",
        "dnd_roll_button": "ทอย {die}",
        "dnd_roll_result": "คุณทอย {die} ได้: {result}",
        "dnd_help_button": "ช่วยเหลือ",
        "dnd_help_title": "ข้อมูลลูกเต๋า",
        "d4_description": "D4 (ลูกเต๋าสี่หน้า) – ใช้สำหรับการทอยความเสียหายเล็กน้อย เช่น มีดสั้นหรือคาถาจรวดเวทมนตร์",
        "d6_description": "D6 (ลูกเต๋าหกหน้า) – ใช้ทั่วไปสำหรับความเสียหายของอาวุธ เช่น ดาบสั้น และยังใช้ในการสร้างตัวละครด้วย",
        "d8_description": "D8 (ลูกเต๋าแปดหน้า) – มักใช้สำหรับอาวุธที่มีความเสียหายปานกลาง เช่น กระบองและคาถาบางอย่าง",
        "d10_description": "D10 (ลูกเต๋าสิบหน้า) – ใช้สำหรับการทอยความเสียหายที่มากขึ้น เช่น อาวุธยุทโธปกรณ์บางชนิดและผลของคาถา",
        "d12_description": "D12 (ลูกเต๋าสิบสองหน้า) – โดยทั่วไปจะใช้สำหรับความเสียหายของอาวุธหนัก เช่น ขวานใหญ่ของคนเถื่อน",
        "d20_description": "D20 (ลูกเต๋ายี่สิบหน้า) – ลูกเต๋าที่สำคัญที่สุด ใช้สำหรับการทอยโจมตี การตรวจสอบทักษะ การทอยป้องกัน และการตัดสินความสำเร็จหรือความล้มเหลว",
        "d100_description": "D100 (ลูกเต๋าเปอร์เซ็นต์) – ใช้สำหรับการทอยเปอร์เซ็นต์ มักใช้ร่วมกับ D10 เพื่อกำหนดผลแบบสุ่มหรือของที่ปล้นมาได้",
        "no_more_names_to_select": "ไม่มีชื่อให้เลือกอีกแล้ว",
        "close_button_text": "ปิด"
    },
    "he": { # Hebrew translations
        "select_language_prompt": "בחר שפה (לדוגמה: en, he): ",
        "language_not_supported": "השפה '{lang}' אינה נתמכת. נעשה שימוש באנגלית.",
        "enter_name_prompt": "הזן את שמך (או הקלד '{quit_cmd}' ליציאה, '{next_cmd}' לבחירת שם): ",
        "exiting_program": "יוצא מהתוכנית.",
        "no_names_to_select": "אין שמות לבחירה. אנא הוסף שמות תחילה.",
        "name_added_to_list": "'{name}' נוסף לרשימה.",
        "congratulations_winner": "מזל טוב {name}! אתה המנצח!",
        "error_no_winner_provided": "שגיאה: לא סופק זוכה לפונקציית הזוכה.",
        "added_to_winners_list": "'{name}' נוסף לרשימת הזוכים.",
        "game_over_all_selected": "המשחק הסתיים! כל השמות נבחרו. הזוכים הם: {winners_list}",
        "names_remaining": "נותרו {count} שמות במאגר הבחירה.",
        "quit_command": "צא",
        "next_command": "הבא",
        "app_title": "בוחר שמות",
        "enter_name_label": "הזן שם:",
        "select_name_button": "בחר שם",
        "add_name_button": "הוסף שם",
        "status_initial": "הוסף שמות ולחץ על 'בחר שם'.",
        "language_dropdown_label": "שפה:",
        "enter_name_prompt_ui": "אנא הזן שם להוספה.",
        "dice_roller_title": "מגלגל קוביות",
        "select_game_label": "בחר משחק לוח:",
        "roll_dice_button": "הטל קוביות",
        "dice_roll_result": "הטלת: {result} (קובייה 1: {d1}, קובייה 2: {d2}) עבור {game}",
        "go_to_dice_roller": "עבור למגלגל קוביות",
        "go_to_name_selector": "עבור לבוחר שמות",
        "dnd_screen_title": "עוזר מבוכים ודרקונים",
        "go_to_dnd_screen": "עבור לעוזר D&D",
        "dnd_roll_button": "הטל {die}",
        "dnd_roll_result": "הטלת {die}: {result}",
        "dnd_help_button": "עזרה",
        "dnd_help_title": "מידע על קוביות",
        "d4_description": "ק4 (קובייה ארבע-פונית) – משמשת לגלגולי נזק קטנים, כגון פגיונות או לחשי טיל קסם.",
        "d6_description": "ק6 (קובייה שש-פונית) – נפוצה לנזקי נשק, כגון חרבות קצרות, ומשמשת גם ביצירת דמויות.",
        "d8_description": "ק8 (קובייה שמונה-פונית) – משמשת לעתים קרובות לכלי נשק עם נזק בינוני, כגון אלות ולחשים מסוימים.",
        "d10_description": "ק10 (קובייה עשר-פונית) – משמשת לגלגולי נזק גדולים יותר, כגון כלי נשק מסוימים ואפקטים של לחשים.",
        "d12_description": "ק12 (קובייה שתים-עשרה-פונית) – משמשת בדרך כלל לנזקי נשק כבדים, כגון גרזן הקרב של ברברי.",
        "d20_description": "ק20 (קובייה עשרים-פונית) – הקובייה החשובה ביותר, משמשת לגלגולי התקפה, בדיקות מיומנות, גלגולי הצלה ולקביעת הצלחה או כישלון.",
        "d100_description": "ק100 (קוביית אחוזים) – משמשת לגלגול אחוזים, לעתים קרובות בשילוב עם ק10 לקביעת אפקטים אקראיים או שלל.",
        "no_more_names_to_select": "לא נותרו עוד שמות לבחירה.",
        "close_button_text": "סגור"
    },
    # --- African Languages ---
    "sw": { # Swahili translations
        "select_language_prompt": "Chagua lugha (k.m. en, sw): ",
        "language_not_supported": "Lugha '{lang}' haitumiki. Inatumia Kiingereza.",
        "enter_name_prompt": "Ingiza jina lako (au andika '{quit_cmd}' kutoka, '{next_cmd}' kuchagua jina): ",
        "exiting_program": "Inatoka kwenye programu.",
        "no_names_to_select": "Hakuna majina ya kuchagua. Tafadhali ongeza majina kwanza.",
        "name_added_to_list": "'{name}' imeongezwa kwenye orodha.",
        "congratulations_winner": "Hongera {name}! Wewe ndiye mshindi!",
        "error_no_winner_provided": "Hitilafu: Hakuna mshindi aliyetolewa kwa chaguo la mshindi.",
        "added_to_winners_list": "'{name}' imeongezwa kwenye orodha ya washindi.",
        "game_over_all_selected": "Mchezo umekwisha! Majina yote yamechaguliwa. Washindi ni: {winners_list}",
        "names_remaining": "Kuna majina {count} yaliyosalia katika dimbwi la uteuzi.",
        "quit_command": "toka",
        "next_command": "ifuatayo",
        "app_title": "Kiteua Jina",
        "enter_name_label": "Ingiza Jina:",
        "select_name_button": "Chagua Jina",
        "add_name_button": "Ongeza Jina",
        "status_initial": "Ongeza majina na ubofye 'Chagua Jina'.",
        "language_dropdown_label": "Lugha:",
        "enter_name_prompt_ui": "Tafadhali ingiza jina la kuongeza.",
        "dice_roller_title": "Kiviringisha Kete",
        "select_game_label": "Chagua Mchezo wa Bodi:",
        "roll_dice_button": "Viringisha Kete",
        "dice_roll_result": "Umeviringisha: {result} (Kete 1: {d1}, Kete 2: {d2}) kwa ajili ya {game}",
        "go_to_dice_roller": "Nenda kwa Kiviringisha Kete",
        "go_to_name_selector": "Nenda kwa Kiteua Jina",
        "dnd_screen_title": "Msaidizi wa Dungeons & Dragons",
        "go_to_dnd_screen": "Nenda kwa Msaidizi wa D&D",
        "dnd_roll_button": "Viringisha {die}",
        "dnd_roll_result": "Umeviringisha {die}: {result}",
        "dnd_help_button": "Msaada",
        "dnd_help_title": "Taarifa za Kete",
        "d4_description": "D4 (kete yenye pande nne) – Hutumika kwa uharibifu mdogo, kama vile visu au miiko ya makombora ya kichawi.",
        "d6_description": "D6 (kete yenye pande sita) – Ya kawaida kwa uharibifu wa silaha, kama panga fupi, na pia hutumika katika uundaji wa wahusika.",
        "d8_description": "D8 (kete yenye pande nane) – Mara nyingi hutumika kwa silaha za uharibifu wa wastani, kama vile rungu na miiko fulani.",
        "d10_description": "D10 (kete yenye pande kumi) – Hutumika kwa uharibifu mkubwa zaidi, kama vile silaha fulani za kivita na athari za miiko.",
        "d12_description": "D12 (kete yenye pande kumi na mbili) – Kwa kawaida hutumika kwa uharibifu wa silaha nzito, kama shoka kubwa la mshenzi.",
        "d20_description": "D20 (kete yenye pande ishirini) – Kete muhimu zaidi, hutumika kwa mashambulizi, majaribio ya ujuzi, mioko ya kuokoa, na kuamua mafanikio au kutofaulu.",
        "d100_description": "D100 (kete ya asilimia) – Hutumika kwa kuviringisha asilimia, mara nyingi pamoja na D10 kuamua athari za nasibu au nyara.",
        "no_more_names_to_select": "Hakuna majina zaidi ya kuchagua.",
        "close_button_text": "Funga"
    },
    "ha": { # Hausa translations
        "select_language_prompt": "Zaɓi harshe (misali en, ha): ",
        "language_not_supported": "Ba a goyon bayan harshen '{lang}'. Ana amfani da Turanci.",
        "enter_name_prompt": "Shigar da sunanka (ko rubuta '{quit_cmd}' don fita, '{next_cmd}' don zaɓar suna): ",
        "exiting_program": "Ana fita daga shirin.",
        "no_names_to_select": "Babu sunaye da zaɓa. Da fatan za a ƙara wasu sunaye da farko.",
        "name_added_to_list": "An ƙara '{name}' zuwa jerin.",
        "congratulations_winner": "Barka {name}! Kai ne mai nasara!",
        "error_no_winner_provided": "Kuskure: Ba a ba da mai nasara ga aikin mai nasara ba.",
        "added_to_winners_list": "An ƙara '{name}' zuwa jerin masu nasara.",
        "game_over_all_selected": "Wasan ya ƙare! An zaɓi duk sunaye. Masu nasara sune: {winners_list}",
        "names_remaining": "Akwai sunaye {count} da suka rage a wurin zaɓi.",
        "quit_command": "fita",
        "next_command": "gaba",
        "app_title": "Mai Zaɓin Suna",
        "enter_name_label": "Shigar da Suna:",
        "select_name_button": "Zaɓi Suna",
        "add_name_button": "Ƙara Suna",
        "status_initial": "Ƙara sunaye kuma danna 'Zaɓi Suna'.",
        "language_dropdown_label": "Harshe:",
        "enter_name_prompt_ui": "Da fatan za a shigar da suna don ƙarawa.",
        "dice_roller_title": "Mai Jefa Kuri'a",
        "select_game_label": "Zaɓi Wasan Allo:",
        "roll_dice_button": "Jefa Kuri'a",
        "dice_roll_result": "Ka jefa: {result} (Kuri'a 1: {d1}, Kuri'a 2: {d2}) don {game}",
        "go_to_dice_roller": "Je zuwa Mai Jefa Kuri'a",
        "go_to_name_selector": "Je zuwa Mai Zaɓin Suna",
        "dnd_screen_title": "Mataimakin Dungeons & Dragons",
        "go_to_dnd_screen": "Je zuwa Mataimakin D&D",
        "dnd_roll_button": "Jefa {die}",
        "dnd_roll_result": "Ka jefa {die}: {result}",
        "dnd_help_button": "Taimako",
        "dnd_help_title": "Bayanin Kuri'a",
        "d4_description": "K4 (kość czworościenna) – Używana do niewielkich rzutów obrażeń, takich jak sztylety lub zaklęcia magicznych pocisków.",
        "d6_description": "K6 (kość sześcienna) – Powszechna dla obrażeń broni, takich jak krótkie miecze, a także używana podczas tworzenia postaci.",
        "d8_description": "K8 (kość ośmiościenna) – Często używana dla broni o umiarkowanych obrażeniach, takich jak buławy i niektóre zaklęcia.",
        "d10_description": "K10 (kość dziesięciościenna) – Używana do większych rzutów obrażeń, takich jak niektóre bronie wojenne i efekty zaklęć.",
        "d12_description": "K12 (kość dwunastościenna) – Zazwyczaj używana do obrażeń ciężkiej broni, takiej jak wielki topór barbarzyńcy.",
        "d20_description": "K20 (kość dwudziestościenna) – Najważniejsza kość, używana do rzutów ataku, testów umiejętności, rzutów obronnych oraz do określania sukcesu lub porażki.",
        "d100_description": "K100 (kość procentowa) – Używana do rzucania procentów, często w połączeniu z K10 do określania losowych efektów lub łupów.",
        "no_more_names_to_select": "Babu sauran sunaye da za a zaɓa.",
        "close_button_text": "Rufe"
    },
    "sv": { # Swedish translations
        "select_language_prompt": "Välj språk (t.ex. en, sv): ",
        "language_not_supported": "Språk '{lang}' stöds inte. Använder engelska.",
        "enter_name_prompt": "Ange ditt namn (eller skriv '{quit_cmd}' för att avsluta, '{next_cmd}' för att välja ett namn): ",
        "exiting_program": "Avslutar programmet.",
        "no_names_to_select": "Inga namn att välja från. Lägg till namn först.",
        "name_added_to_list": "'{name}' tillagd i listan.",
        "congratulations_winner": "Grattis {name}! Du är vinnaren!",
        "error_no_winner_provided": "Fel: Ingen vinnare angavs till vinnarfunktionen.",
        "added_to_winners_list": "'{name}' har lagts till i vinnarlistan.",
        "game_over_all_selected": "Spelet är över! Alla namn har valts. Vinnarna är: {winners_list}",
        "names_remaining": "Det finns {count} namn kvar i urvalspoolen.",
        "quit_command": "avsluta",
        "next_command": "nästa",
        "app_title": "Namnväljare",
        "enter_name_label": "Ange ett Namn:",
        "select_name_button": "Välj Namn",
        "add_name_button": "Lägg till Namn",
        "status_initial": "Lägg till namn och klicka på 'Välj Namn'.",
        "language_dropdown_label": "Språk:",
        "enter_name_prompt_ui": "Ange ett namn att lägga till.",
        "dice_roller_title": "Tärningskastare",
        "select_game_label": "Välj Brädspel:",
        "roll_dice_button": "Kasta Tärning",
        "dice_roll_result": "Du slog: {result} (Tärning 1: {d1}, Tärning 2: {d2}) för {game}",
        "go_to_dice_roller": "Gå till Tärningskastare",
        "go_to_name_selector": "Gå till Namnväljare",
        "dnd_screen_title": "Dungeons & Dragons Hjälpreda",
        "go_to_dnd_screen": "Gå till D&D Hjälpreda",
        "dnd_roll_button": "Slå {die}",
        "dnd_roll_result": "Du slog en {die}: {result}",
        "dnd_help_button": "Hjälp",
        "dnd_help_title": "Tärningsinformation",
        "d4_description": "T4 (fyrsidig tärning) – Används för små skadeslag, som dolkar eller trollformler med magiska projektiler.",
        "d6_description": "T6 (sexsidig tärning) – Vanlig för vapenskada, som korta svärd, och används även vid karaktärsskapande.",
        "d8_description": "T8 (åttasidig tärning) – Används ofta för vapen med måttlig skada, som stridsklubbor och vissa trollformler.",
        "d10_description": "T10 (tiosidig tärning) – Används för större skadeslag, som vissa stridsvapen och trollformelseffekter.",
        "d12_description": "T12 (tolvsidig tärning) – Används vanligtvis för tung vapenskada, som en barbars stridsyxa.",
        "d20_description": "T20 (tjugosidig tärning) – Den viktigaste tärningen, används för attackslag, färdighetsslag, räddningsslag och för att avgöra framgång eller misslyckande.",
        "d100_description": "T100 (procenttärning) – Används för att slå procent, ofta tillsammans med en T10 för att avgöra slumpmässiga effekter eller byte.",
        "no_more_names_to_select": "Inga fler namn att välja.",
        "close_button_text": "Stäng" # Re-added for consistency
    },
    "zh-CN": { # Simplified Chinese translations
        "select_language_prompt": "选择语言 (例如: en, es): ",
        "language_not_supported": "不支持语言 '{lang}'。正在使用英语。",
        "enter_name_prompt": "输入您的名字 (或输入 '{quit_cmd}' 退出, '{next_cmd}' 选择名字): ",
        "exiting_program": "正在退出程序。",
        "no_names_to_select": "没有可供选择的名字。请先添加一些名字。",
        "name_added_to_list": "已将 '{name}' 添加到列表中。",
        "congratulations_winner": "恭喜 {name}! 您是赢家!",
        "error_no_winner_provided": "错误：没有为赢家功能提供赢家。",
        "added_to_winners_list": "'{name}' 已添加到赢家列表中。",
        "game_over_all_selected": "游戏结束！所有名字都已被选中。赢家是: {winners_list}",
        "names_remaining": "选择池中还剩 {count} 个名字。",
        "quit_command": "退出",
        "next_command": "下一个",
        # New keys for GUI
        "app_title": "名称选择器",
        "enter_name_label": "输入名称:",
        "select_name_button": "选择名称",
        "add_name_button": "添加名称",
        "status_initial": "添加名称并点击“选择名称”。",
        "language_dropdown_label": "语言:",
        "enter_name_prompt_ui": "请输入要添加的名称。",
        "dice_roller_title": "掷骰子",
        "select_game_label": "选择棋盘游戏:",
        "roll_dice_button": "掷骰子",
        "dice_roll_result": "您掷出了: {result} (骰子 1: {d1}, 骰子 2: {d2}) 用于 {game}",
        "go_to_dice_roller": "前往掷骰子",
        "go_to_name_selector": "前往名称选择器",
        "dnd_screen_title": "龙与地下城助手",
        "go_to_dnd_screen": "前往D&D助手",
        "dnd_roll_button": "掷 {die}",
        "dnd_roll_result": "您掷出了一个 {die}: {result}",
        "dnd_help_button": "帮助",
        "dnd_help_title": "骰子信息",
        "d4_description": "D4 (四面骰) – 用于小型伤害掷骰，例如匕首或魔法飞弹法术。",
        "d6_description": "D6 (六面骰) – 常用于武器伤害，例如短剑，也用于角色创建。",
        "d8_description": "D8 (八面骰) – 常用于中等伤害武器，例如钉头锤和某些法术。",
        "d10_description": "D10 (十面骰) – 用于较大的伤害掷骰，例如某些军用武器和法术效果。",
        "d12_description": "D12 (十二面骰) – 通常用于重型武器伤害，例如野蛮人的巨斧。",
        "d20_description": "D20 (二十面骰) – 最重要的骰子，用于攻击掷骰、技能检定、豁免检定以及确定成功或失败。",
        "d100_description": "D100 (百分骰) – 用于掷百分比，通常与D10结合使用以确定随机效果或战利品。",
        "no_more_names_to_select": "没有更多名称可供选择。",
        "close_button_text": "关闭"
    },
    "zh-TW": { # Traditional Chinese translations
        "select_language_prompt": "選擇語言 (例如: en, es): ",
        "language_not_supported": "不支持語言 '{lang}'。正在使用英語。",
        "enter_name_prompt": "輸入您的名字 (或輸入 '{quit_cmd}' 退出, '{next_cmd}' 選擇名字): ",
        "exiting_program": "正在退出程式。",
        "no_names_to_select": "沒有可供選擇的名字。請先添加一些名字。",
        "name_added_to_list": "已將 '{name}' 添加到列表中。",
        "congratulations_winner": "恭喜 {name}! 您是贏家!",
        "error_no_winner_provided": "錯誤：沒有為贏家功能提供贏家。",
        "added_to_winners_list": "'{name}' 已添加到贏家列表中。",
        "game_over_all_selected": "遊戲結束！所有名字都已被選中。贏家是: {winners_list}",
        "names_remaining": "選擇池中還剩 {count} 個名字。",
        "quit_command": "退出",
        "next_command": "下一個",
        # New keys for GUI
        "app_title": "名稱選擇器",
        "enter_name_label": "輸入名稱:",
        "select_name_button": "選擇名稱",
        "add_name_button": "新增名稱",
        "status_initial": "新增名稱並點擊「選擇名稱」。",
        "language_dropdown_label": "語言:",
        "enter_name_prompt_ui": "請輸入要新增的名稱。",
        "dice_roller_title": "擲骰子",
        "select_game_label": "選擇桌遊:",
        "roll_dice_button": "擲骰子",
        "dice_roll_result": "您擲出了: {result} (骰子 1: {d1}, 骰子 2: {d2}) 用於 {game}",
        "go_to_dice_roller": "前往擲骰子",
        "go_to_name_selector": "前往名稱選擇器",
        "dnd_screen_title": "龍與地下城助手",
        "go_to_dnd_screen": "前往D&D助手",
        "dnd_roll_button": "擲 {die}",
        "dnd_roll_result": "您擲出了一個 {die}: {result}",
        "dnd_help_button": "幫助",
        "dnd_help_title": "骰子資訊",
        "d4_description": "D4 (四面骰) – 用於小型傷害擲骰，例如匕首或魔法飛彈法術。",
        "d6_description": "D6 (六面骰) – 常用於武器傷害，例如短劍，也用於角色創建。",
        "d8_description": "D8 (八面骰) – 常用於中等傷害武器，例如釘頭錘和某些法術。",
        "d10_description": "D10 (十面骰) – 用於較大的傷害擲骰，例如某些軍用武器和法術效果。",
        "d12_description": "D12 (十二面骰) – 通常用於重型武器傷害，例如野蠻人的巨斧。",
        "d20_description": "D20 (二十面骰) – 最重要的骰子，用於攻擊擲骰、技能檢定、豁免檢定以及確定成功或失敗。",
        "d100_description": "D100 (百分骰) – 用於擲百分比，通常與D10結合使用以確定隨機效果或戰利品。",
        "no_more_names_to_select": "沒有更多名稱可供選擇。",
        "close_button_text": "關閉"
    }
}
boardgames=["Monopoly", "Risk", "Settlers of Catan", "Axis & Allies", "Backgammon", "Clue", "The Game of Life", "Ludo",
            "Can't Stop", "Chicago Express", "Formula D", "Las Vegas", "Shut the Box", "Trouble", "Yahtzee", "King of Tokyo",
            "Dice Forge", "Roll for the Galaxy", "Stone Age", "Machi Koro", "Liar’s Dice", "Zombie Dice", "Qwixx", 
            "Betrayal at House on the Hill", "Descent: Legends of the Dark", "Nemesis", "Brikks", "King of the Dice", "Ruin It",
            "Wits & Wagers Deluxe", "Mahadev Jumbo Sequence", "Santa’s Rooftop Scramble", "One Night Ultimate Alien"

]
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

import tkinter as tk
from tkinter import ttk

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
    name_selector_frame.pack(fill="both", expand=True)
    update_ui_language() # Refresh button text

def show_dice_roller_frame():
    name_selector_frame.pack_forget()
    dnd_frame.pack_forget() # Hide D&D frame
    dice_roller_frame.pack(fill="both", expand=True)
    update_ui_language() # Refresh button text

def show_dnd_frame():
    name_selector_frame.pack_forget()
    dice_roller_frame.pack_forget()
    dnd_frame.pack(fill="both", expand=True)
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
    global dnd_roll_d4_button, dnd_roll_d6_button, dnd_roll_d8_button, dnd_roll_d10_button, dnd_roll_d12_button, dnd_roll_d20_button, dnd_roll_d100_button, dnd_help_button # D&D buttons

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


# ---------- Main Window ----------
root = tk.Tk()
root.geometry("400x600") # Increased height for D&D screen elements
root.configure(bg=BG_COLOR)

# ---------- Frames for different screens ----------
name_selector_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
dice_roller_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
dnd_frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame') # D&D Frame

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

name_selector_to_dice_button = ttk.Button(name_selector_frame, command=show_dice_roller_frame)
name_selector_to_dice_button.pack(pady=(10,0), side=tk.LEFT, expand=True)

name_selector_to_dnd_button = ttk.Button(name_selector_frame, command=show_dnd_frame)
name_selector_to_dnd_button.pack(pady=(10,0), side=tk.RIGHT, expand=True)

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

dice_roller_to_name_button = ttk.Button(dice_roller_frame, command=show_name_selector_frame)
dice_roller_to_name_button.pack(pady=(10,0), side=tk.LEFT, expand=True)

dice_roller_to_dnd_button = ttk.Button(dice_roller_frame, command=show_dnd_frame)
dice_roller_to_dnd_button.pack(pady=(10,0), side=tk.RIGHT, expand=True)

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
dnd_to_name_selector_button.pack(side=tk.LEFT, expand=True, padx=5)

dnd_to_dice_roller_button = ttk.Button(dnd_nav_frame, command=show_dice_roller_frame)
dnd_to_dice_roller_button.pack(side=tk.RIGHT, expand=True, padx=5)

# Initial UI language setup and frame display
show_name_selector_frame() # Show name selector by default
update_ui_language(current_language) 

# ---------- Run the App (moved to if __name__ == "__main__") ----------

# --- CLI Functions (renamed) ---
def get_message_cli(key, **kwargs): # Renamed to avoid conflict if we want separate CLI/GUI get_message
    global current_language
    
    message_template = translations.get(current_language, translations["en"]).get(key, translations["en"].get(key))
    if message_template is None:
        return key 
    return message_template.format(**kwargs)

def set_language_cli():
    """Allows the user to select a language for CLI."""
    global current_language
   
    lang_code = input(translations["en"]["select_language_prompt"]).strip().lower()
    if lang_code in translations:
        current_language = lang_code
    else:
        print(translations["en"]["language_not_supported"].format(lang=lang_code))
        current_language = "en" 

def main_cli(names_list):
    while True:
        name_input = input(get_message_cli("enter_name_prompt", quit_cmd=get_message_cli("quit_command"), next_cmd=get_message_cli("next_command")))
        if name_input.lower() == get_message_cli("quit_command"):
            print(get_message_cli("exiting_program"))
            break
        elif name_input.lower() == get_message_cli("next_command"):
            if not names_list:
                print(get_message_cli("no_names_to_select"))
            else:
                selected_winner_name = make_selection(names_list)
                if selected_winner_name:
                    winner(selected_winner_name)
        else:
            names_list.append(name_input)
            print(get_message_cli("name_added_to_list", name=name_input))

def make_selection(current_names):
    if not current_names:
        print(get_message_cli("no_names_to_select"))
        return None
    
    selected_name = random.choice(current_names)
    print(get_message_cli("congratulations_winner", name=selected_name))
    current_names.remove(selected_name)
    return selected_name

def winner(name_of_the_winner):
    if name_of_the_winner is None:
        print(get_message_cli("error_no_winner_provided"))
        return

    winners.append(name_of_the_winner)
    print(get_message_cli("added_to_winners_list", name=name_of_the_winner))

    if not names: # Check the global names list
        print(get_message_cli("game_over_all_selected", winners_list=winners))
    else:
        print(get_message_cli("names_remaining", count=len(names)))

# --- End of CLI Functions ---

if __name__ == "__main__":
    # To run CLI version:
    # set_language_cli() 
    # main_cli(names)
    
    # To run GUI version:
    root.mainloop()
