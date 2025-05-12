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
        "enter_name_prompt_ui": "Please enter a name to add."
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
        "enter_name_prompt_ui": "Por favor, introduce un nombre para añadir."
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
        "enter_name_prompt_ui": "Bitte geben Sie einen Namen ein, um ihn hinzuzufügen."
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
        "enter_name_prompt_ui": "Veuillez entrer un nom à ajouter."
    },
    "it": { # Italian translations
        "select_language_prompt": "Seleziona la lingua (es. en, it): ",
        "language_not_supported": "Lingua '{lang}' non supportata. Si utilizza l'inglese.",
        "enter_name_prompt": "Inserisci il tuo nome (o digita '{quit_cmd}' per uscire, '{next_cmd}' per selezionare un nome): ",
        "exiting_program": "Uscita dal programma.",
        "no_names_to_select": "Nessun nome da selezionare. Aggiungi prima dei nomi.",
        "name_added_to_list": "'{name}' aggiunto alla lista.",
        "congratulations_winner": "Congratulazioni {name}! Sei il vincitore!",
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
        "enter_name_prompt_ui": "Inserisci un nome da aggiungere."
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
        "enter_name_prompt_ui": "Por favor, digite um nome para adicionar."
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
        "enter_name_prompt_ui": "Voer een naam in om toe te voegen."
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
        "enter_name_prompt_ui": "Wpisz imię, aby dodać."
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
        "enter_name_prompt_ui": "Ange ett namn att lägga till."
    },
    "el": { # Greek translations
        "select_language_prompt": "Επιλέξτε γλώσσα (π.χ. en, el): ",
        "language_not_supported": "Η γλώσσα '{lang}' δεν υποστηρίζεται. Χρήση Αγγλικών.",
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
        "enter_name_prompt_ui": "Παρακαλώ εισαγάγετε ένα όνομα για προσθήκη."
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
        "enter_name_prompt_ui": "Пожалуйста, введите имя для добавления."
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
        "enter_name_prompt_ui": "追加する名前を入力してください。"
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
        "enter_name_prompt_ui": "추가할 이름을 입력하세요."
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
        "enter_name_prompt_ui": "कृपया जोड़ने के लिए एक नाम दर्ज करें।"
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
        "enter_name_prompt_ui": "الرجاء إدخال اسم لإضافته."
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
        "enter_name_prompt_ui": "Lütfen eklenecek bir isim girin."
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
        "enter_name_prompt_ui": "Vui lòng nhập tên để thêm."
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
        "enter_name_prompt_ui": "โปรดป้อนชื่อที่จะเพิ่ม"
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
        "enter_name_prompt_ui": "אנא הזן שם להוספה."
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
        "enter_name_prompt_ui": "Tafadhali ingiza jina la kuongeza."
    },
    "ha": { # Hausa translations
        "select_language_prompt": "Zaɓi harshe (misali en, ha): ",
        "language_not_supported": "Ba a goyon bayan harshen '{lang}'. Ana amfani da Turanci.",
        "enter_name_prompt": "Shigar da sunanka (ko rubuta '{quit_cmd}' don fita, '{next_cmd}' don zaɓar suna): ",
        "exiting_program": "Ana fita daga shirin.",
        "no_names_to_select": "Babu sunaye da za a zaɓa. Da fatan za a ƙara wasu sunaye da farko.",
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
        "enter_name_prompt_ui": "Da fatan za a shigar da suna don ƙarawa."
    },
    "yo": { # Yoruba translations
        "select_language_prompt": "Yan èdè (àpẹẹrẹ, en, yo): ",
        "language_not_supported": "Èdè '{lang}' kò sí. A ó lo Gẹ̀ẹ́sì.",
        "enter_name_prompt": "Tẹ orúkọ rẹ (tàbí tẹ '{quit_cmd}' láti jáde, '{next_cmd}' láti yan orúkọ): ",
        "exiting_program": "Ó ń jáde kúrò nínú ètò.",
        "no_names_to_select": "Kò sí orúkọ láti yàn. Jọ̀wọ́, kọ́kọ́ fi àwọn orúkọ kún un.",
        "name_added_to_list": "A ti fi '{name}' kún àkójọ.",
        "congratulations_winner": "Oriire {name}! Ìwọ ni olùborí!",
        "error_no_winner_provided": "Àṣìṣe: A kò pèsè olùborí fún iṣẹ́ olùborí.",
        "added_to_winners_list": "A ti fi '{name}' kún àkójọ àwọn olùborí.",
        "game_over_all_selected": "Eré ti parí! A ti yan gbogbo orúkọ. Àwọn olùborí ni: {winners_list}",
        "names_remaining": "Orúkọ {count} ló ṣẹ́ kù nínú àkójọpọ̀ yíyàn.",
        "quit_command": "jáde",
        "next_command": "tókàn",
        "app_title": "Aṣàyàn Orúkọ",
        "enter_name_label": "Tẹ Orúkọ Kan:",
        "select_name_button": "Yan Orúkọ",
        "add_name_button": "Fi Orúkọ Kún",
        "status_initial": "Fi àwọn orúkọ kún un kí o sì tẹ 'Yan Orúkọ'.",
        "language_dropdown_label": "Èdè:",
        "enter_name_prompt_ui": "Jọ̀wọ́, tẹ orúkọ kan láti fi kún un."
    },
    "zu": { # Zulu translations
        "select_language_prompt": "Khetha ulimi (isb. en, zu): ",
        "language_not_supported": "Ulimi '{lang}' alusekelwe. Kusetshenziswa isiNgisi.",
        "enter_name_prompt": "Faka igama lakho (noma thayipha '{quit_cmd}' ukuphuma, '{next_cmd}' ukukhetha igama): ",
        "exiting_program": "Iphuma ohlelweni.",
        "no_names_to_select": "Awekho amagama okukhetha kuwo. Sicela ungeze amagama kuqala.",
        "name_added_to_list": "'{name}' kungezwe ohlwini.",
        "congratulations_winner": "Siyakuhalalisela {name}! Nguwe owinile!",
        "error_no_winner_provided": "Iphutha: Akunikezwanga owinile emsebenzini wokuwina.",
        "added_to_winners_list": "'{name}' kungezwe ohlwini lwabawinile.",
        "game_over_all_selected": "Umdlalo uphelile! Wonke amagama akhethiwe. Abawinile yilaba: {winners_list}",
        "names_remaining": "Kusele amagama angu-{count} endaweni yokukhetha.",
        "quit_command": "phuma",
        "next_command": "okulandelayo",
        "app_title": "Isikhethi Samagama",
        "enter_name_label": "Faka Igama:",
        "select_name_button": "Khetha Igama",
        "add_name_button": "Engeza Igama",
        "status_initial": "Engeza amagama bese uchofoza 'Khetha Igama'.",
        "language_dropdown_label": "Ulimi:",
        "enter_name_prompt_ui": "Sicela ufake igama ozolengeza."
    },
    "am": { # Amharic translations
        "select_language_prompt": "ቋንቋ ይምረጡ (ለምሳሌ en, am): ",
        "language_not_supported": "ቋንቋ '{lang}' አይደገፍም። እንግሊዝኛ ጥቅም ላይ እየዋለ ነው።",
        "enter_name_prompt": "ስምዎን ያስገቡ (ወይም ለመውጣት '{quit_cmd}' ይተይቡ፣ ስም ለመምረጥ '{next_cmd}' ይተይቡ): ",
        "exiting_program": "ከፕሮግራሙ በመውጣት ላይ።",
        "no_names_to_select": "የሚመረጡ ስሞች የሉም። እባክዎ መጀመሪያ አንዳንድ ስሞችን ያክሉ።",
        "name_added_to_list": "'{name}' ወደ ዝርዝሩ ታክሏል።",
        "congratulations_winner": "እንኳን ደስ አለዎት {name}! እርስዎ አሸናፊ ነዎት!",
        "error_no_winner_provided": "ስህተት፡ ለአሸናፊ ተግባር ምንም አሸናፊ አልቀረበም።",
        "added_to_winners_list": "'{name}' ወደ አሸናፊዎች ዝርዝር ታክሏል።",
        "game_over_all_selected": "ጨዋታው አልቋል! ሁሉም ስሞች ተመርጠዋል። አሸናፊዎቹ፡ {winners_list}",
        "names_remaining": "በምርጫ ገንዳ ውስጥ {count} ስሞች ቀርተዋል።",
        "quit_command": "ውጣ",
        "next_command": "ቀጣይ",
        "app_title": "ስም መራጭ",
        "enter_name_label": "ስም ያስገቡ:",
        "select_name_button": "ስም ይምረጡ",
        "add_name_button": "ስም ያክሉ",
        "status_initial": "ስሞችን ያክሉ እና 'ስም ይምረጡ' የሚለውን ጠቅ ያድርጉ።",
        "language_dropdown_label": "ቋንቋ:",
        "enter_name_prompt_ui": "እባክዎ ለማከል ስም ያስገቡ።"
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
        "enter_name_prompt_ui": "请输入要添加的名称。"
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
        "enter_name_prompt_ui": "請輸入要新增的名稱。"
    }
}

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

# ---------- GUI Functions ----------
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
            display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\nNo more names to select.")
        else: # No names were ever added
            display_var.set(get_message("no_names_to_select"))

# ---------- Language Selection Functions ----------
def update_ui_language(lang_code=None):
    """Updates all UI text elements to the selected language."""
    global current_language, root, title_label, select_button, add_name_button, display_var, lang_combo_label
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
    
    # Update status message based on current game state or set to initial
    if not names and not winners:
        display_var.set(get_message("status_initial"))
    elif not names and winners: # Game is over
        winners_text = ", ".join(f"{i+1}. {w}" for i, w in enumerate(winners))
        display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\n" + get_message("no_names_to_select"))
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
        display_var.set(get_message("game_over_all_selected", winners_list=winners_text) + "\n" + get_message("no_names_to_select"))
    elif not names and not winners:
        display_var.set(get_message("status_initial"))


# ---------- Main Window ----------
root = tk.Tk()
root.geometry("400x350") # Increased height for language dropdown

# ---------- Style Configuration ----------
style = ttk.Style()
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
# Language Selector
lang_combo_label = ttk.Label(root) # Text will be set by update_ui_language
lang_combo_label.pack(pady=(10,0))

language_options = list(translations.keys())
language_var = tk.StringVar(value=current_language)
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=language_options, state="readonly", width=38)
language_dropdown.pack(pady=(0,10))
language_dropdown.bind("<<ComboboxSelected>>", on_language_select)

title_label = ttk.Label(root, font=FONT_TITLE) # Text will be set by update_ui_language
title_label.pack(pady=(5, 10)) # Adjusted padding

name_entry = ttk.Entry(root, width=30)
name_entry.pack(pady=5)

select_button = ttk.Button(root, command=select_name_ui) # Text will be set by update_ui_language
select_button.pack(pady=10)

add_name_button = ttk.Button(root, command=add_name_ui) # Text will be set by update_ui_language
add_name_button.pack(pady=5)

display_var = tk.StringVar()
display_label = ttk.Label(root, textvariable=display_var, font=FONT_DISPLAY, foreground=PRIMARY_COLOR, wraplength=380)
display_label.pack(pady=(10, 10)) # Adjusted padding

# Initial UI language setup
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
