import random

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
        "next_command": "next"
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
        "next_command": "siguiente"
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
        "next_command": "weiter"
    },
    "el": { # Greek translations
        "select_language_prompt": "Επιλέξτε γλώσσα (π.χ. en, es, ger, el, ar, fi, sv, ru, pt): ",
        "language_not_supported": "Η γλώσσα '{lang}' δεν υποστηρίζεται. Χρήση Αγγλικών.",
        "enter_name_prompt": "Εισαγάγετε το όνομά σας (ή πληκτρολογήστε '{quit_cmd}' για έξοδο, '{next_cmd}' για επιλογή ονόματος): ",
        "exiting_program": "Έξοδος από το πρόγραμμα.",
        "no_names_to_select": "Δεν υπάρχουν ονόματα για επιλογή. Προσθέστε πρώτα μερικά ονόματα.",
        "name_added_to_list": "Το '{name}' προστέθηκε στη λίστα.",
        "congratulations_winner": "Συγχαρητήρια {name}! Είσαι ο νικητής!",
        "error_no_winner_provided": "Σφάλμα: Δεν δόθηκε νικητής στη συνάρτηση νικητή.",
        "added_to_winners_list": "Το '{name}' προστέθηκε στη λίστα νικητών.",
        "game_over_all_selected": "Το παιχνίδι τελείωσε! Όλα τα ονόματα έχουν επιλεγεί. Οι νικητές είναι: {winners_list}",
        "names_remaining": "Απομένουν {count} ονόματα στην ομάδα επιλογής.",
        "quit_command": "έξοδος",
        "next_command": "επόμενο"
    },
    "ar": { # Arabic translations
        "select_language_prompt": "اختر اللغة (مثل en, es, ger, el, ar, fi, sv, ru, pt): ",
        "language_not_supported": "اللغة '{lang}' غير مدعومة. سيتم استخدام الإنجليزية.",
        "enter_name_prompt": "أدخل اسمك (أو اكتب '{quit_cmd}' للخروج، '{next_cmd}' لاختيار اسم): ",
        "exiting_program": "الخروج من البرنامج.",
        "no_names_to_select": "لا توجد أسماء للاختيار من بينها. الرجاء إضافة بعض الأسماء أولاً.",
        "name_added_to_list": "تمت إضافة '{name}' إلى القائمة.",
        "congratulations_winner": "تهانينا {name}! أنت الفائز!",
        "error_no_winner_provided": "خطأ: لم يتم تقديم فائز لدالة الفائز.",
        "added_to_winners_list": "تمت إضافة '{name}' إلى قائمة الفائزين.",
        "game_over_all_selected": "انتهت اللعبة! تم اختيار جميع الأسماء. الفائزون هم: {winners_list}",
        "names_remaining": "يوجد {count} أسماء متبقية في مجموعة الاختيار.",
        "quit_command": "خروج",
        "next_command": "التالي"
    },
    "fi": { # Finnish translations
        "select_language_prompt": "Valitse kieli (esim. en, es): ",
        "language_not_supported": "Kieli '{lang}' ei ole tuettu. Käytetään englantia.",
        "enter_name_prompt": "Kirjoita nimesi (tai '{quit_cmd}' poistuaksesi, '{next_cmd}' valitaksesi nimen): ",
        "exiting_program": "Poistutaan ohjelmasta.",
        "no_names_to_select": "Ei valittavia nimiä. Lisää ensin nimiä.",
        "name_added_to_list": "'{name}' lisätty listaan.",
        "congratulations_winner": "Onneksi olkoon {name}! Olet voittaja!",
        "error_no_winner_provided": "Virhe: Voittajaa ei annettu voittajafunktiolle.",
        "added_to_winners_list": "'{name}' on lisätty voittajien listaan.",
        "game_over_all_selected": "Peli on ohi! Kaikki nimet on valittu. Voittajat ovat: {winners_list}",
        "names_remaining": "Valintajoukossa on jäljellä {count} nimeä.",
        "quit_command": "lopeta",
        "next_command": "seuraava"
    },
    "sv": { # Swedish translations
        "select_language_prompt": "Välj språk (t.ex. en, es): ",
        "language_not_supported": "Språket '{lang}' stöds inte. Använder engelska.",
        "enter_name_prompt": "Ange ditt namn (eller skriv '{quit_cmd}' för att avsluta, '{next_cmd}' för att välja ett namn): ",
        "exiting_program": "Avslutar programmet.",
        "no_names_to_select": "Inga namn att välja från. Lägg till några namn först.",
        "name_added_to_list": "'{name}' har lagts till i listan.",
        "congratulations_winner": "Grattis {name}! Du är vinnaren!",
        "error_no_winner_provided": "Fel: Ingen vinnare angavs till vinnarfunktionen.",
        "added_to_winners_list": "'{name}' har lagts till i vinnarlistan.",
        "game_over_all_selected": "Spelet är över! Alla namn har valts. Vinnarna är: {winners_list}",
        "names_remaining": "Det finns {count} namn kvar i urvalspoolen.",
        "quit_command": "avsluta",
        "next_command": "nästa"
    },
    "ru": { # Russian translations
        "select_language_prompt": "Выберите язык (например, en, es): ",
        "language_not_supported": "Язык '{lang}' не поддерживается. Используется английский.",
        "enter_name_prompt": "Введите ваше имя (или '{quit_cmd}' для выхода, '{next_cmd}' для выбора имени): ",
        "exiting_program": "Выход из программы.",
        "no_names_to_select": "Нет имен для выбора. Пожалуйста, сначала добавьте имена.",
        "name_added_to_list": "Имя '{name}' добавлено в список.",
        "congratulations_winner": "Поздравляем {name}! Вы победитель!",
        "error_no_winner_provided": "Ошибка: Победитель не был предоставлен функции победителя.",
        "added_to_winners_list": "Имя '{name}' добавлено в список победителей.",
        "game_over_all_selected": "Игра окончена! Все имена выбраны. Победители: {winners_list}",
        "names_remaining": "В пуле выбора осталось {count} имен.",
        "quit_command": "выход",
        "next_command": "далее"
    },
    "pt": { # Portuguese translations
        "select_language_prompt": "Selecione o idioma (ex: en, es): ",
        "language_not_supported": "Idioma '{lang}' não suportado. Usando inglês.",
        "enter_name_prompt": "Digite seu nome (ou '{quit_cmd}' para sair, '{next_cmd}' para selecionar um nome): ",
        "exiting_program": "Saindo do programa.",
        "no_names_to_select": "Nenhum nome para selecionar. Adicione alguns nomes primeiro.",
        "name_added_to_list": "Nome '{name}' adicionado à lista.",
        "congratulations_winner": "Parabéns {name}! Você é o vencedor!",
        "error_no_winner_provided": "Erro: Nenhum vencedor foi fornecido para a função de vencedor.",
        "added_to_winners_list": "Nome '{name}' foi adicionado à lista de vencedores.",
        "game_over_all_selected": "Jogo terminado! Todos os nomes foram selecionados. Os vencedores são: {winners_list}",
        "names_remaining": "Restam {count} nomes no pool de seleção.",
        "quit_command": "sair",
        "next_command": "próximo"
    },
    "uk": { # Ukrainian translations
        "select_language_prompt": "Виберіть мову (наприклад, en, es): ",
        "language_not_supported": "Мова '{lang}' не підтримується. Використовується англійська.",
        "enter_name_prompt": "Введіть ваше ім'я (або '{quit_cmd}' для виходу, '{next_cmd}' для вибору імені): ",
        "exiting_program": "Вихід з програми.",
        "no_names_to_select": "Немає імен для вибору. Будь ласка, спочатку додайте імена.",
        "name_added_to_list": "Ім'я '{name}' додано до списку.",
        "congratulations_winner": "Вітаємо {name}! Ви переможець!",
        "error_no_winner_provided": "Помилка: Переможця не було надано функції переможця.",
        "added_to_winners_list": "Ім'я '{name}' додано до списку переможців.",
        "game_over_all_selected": "Гру закінчено! Всі імена вибрано. Переможці: {winners_list}",
        "names_remaining": "Залишилося {count} імен у пулі вибору.",
        "quit_command": "вихід",
        "next_command": "далі"
    },
    "pa": { # Punjabi translations
        "select_language_prompt": "ਭਾਸ਼ਾ ਚੁਣੋ (ਮਿਸਾਲ ਵਜੋਂ, en, es): ",
        "language_not_supported": "ਭਾਸ਼ਾ '{lang}' ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ। ਅੰਗਰੇਜ਼ੀ ਵਰਤੀ ਜਾ ਰਹੀ ਹੈ।",
        "enter_name_prompt": "ਆਪਣਾ ਨਾਮ ਦਰਜ ਕਰੋ (ਜਾਂ ਬਾਹਰ ਨਿਕਲਣ ਲਈ '{quit_cmd}', ਨਾਮ ਚੁਣਨ ਲਈ '{next_cmd}' ਟਾਈਪ ਕਰੋ): ",
        "exiting_program": "ਪ੍ਰੋਗਰਾਮ ਤੋਂ ਬਾਹਰ ਨਿਕਲ ਰਹੇ ਹਾਂ।",
        "no_names_to_select": "ਚੁਣਨ ਲਈ ਕੋਈ ਨਾਮ ਨਹੀਂ। ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਕੁਝ ਨਾਮ ਸ਼ਾਮਲ ਕਰੋ।",
        "name_added_to_list": "ਨਾਮ '{name}' ਸੂਚੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਗਿਆ ਹੈ।",
        "congratulations_winner": "ਮੁਬਾਰਕਾਂ {name}! ਤੁਸੀਂ ਜੇਤੂ ਹੋ!",
        "error_no_winner_provided": "ਗਲਤੀ: ਜੇਤੂ ਫੰਕਸ਼ਨ ਨੂੰ ਕੋਈ ਜੇਤੂ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ।",
        "added_to_winners_list": "ਨਾਮ '{name}' ਜੇਤੂਆਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰ ਦਿੱਤਾ ਗਿਆ ਹੈ।",
        "game_over_all_selected": "ਖੇਡ ਖਤਮ! ਸਾਰੇ ਨਾਮ ਚੁਣ ਲਏ ਗਏ ਹਨ। ਜੇਤੂ ਹਨ: {winners_list}",
        "names_remaining": "ਚੋਣ ਪੂਲ ਵਿੱਚ {count} ਨਾਮ ਬਾਕੀ ਹਨ।",
        "quit_command": "ਬਾਹਰ",
        "next_command": "ਅਗਲਾ"
    },
    "gu": { # Gujarati translations
        "select_language_prompt": "ભાષા પસંદ કરો (દા.ત., en, es): ",
        "language_not_supported": "ભાષા '{lang}' સમર્થિત નથી. અંગ્રેજી વપરાઈ રહી છે.",
        "enter_name_prompt": "તમારું નામ દાખલ કરો (અથવા બહાર નીકળવા માટે '{quit_cmd}', નામ પસંદ કરવા માટે '{next_cmd}' ટાઇપ કરો): ",
        "exiting_program": "પ્રોગ્રામમાંથી બહાર નીકળી રહ્યા છીએ.",
        "no_names_to_select": "પસંદ કરવા માટે કોઈ નામ નથી. કૃપા કરીને પહેલા કેટલાક નામ ઉમેરો.",
        "name_added_to_list": "નામ '{name}' યાદીમાં ઉમેરાયું.",
        "congratulations_winner": "અભિનંદન {name}! તમે વિજેતા છો!",
        "error_no_winner_provided": "ભૂલ: વિજેતા કાર્યને કોઈ વિજેતા પ્રદાન કરવામાં આવ્યો ન હતો.",
        "added_to_winners_list": "નામ '{name}' વિજેતાઓની યાદીમાં ઉમેરવામાં આવ્યું છે.",
        "game_over_all_selected": "રમત સમાપ્ત! બધા નામો પસંદ કરવામાં આવ્યા છે. વિજેતાઓ છે: {winners_list}",
        "names_remaining": "પસંદગી પૂલમાં {count} નામો બાકી છે.",
        "quit_command": "બહાર",
        "next_command": "આગળ"
    },
    "kn": { # Kannada translations
        "select_language_prompt": "ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ (ಉದಾ, en, es): ",
        "language_not_supported": "ಭಾಷೆ '{lang}' ಬೆಂಬಲಿತವಾಗಿಲ್ಲ. ಇಂಗ್ಲಿಷ್ ಬಳಸಲಾಗುತ್ತಿದೆ.",
        "enter_name_prompt": "ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ (ಅಥವಾ ನಿರ್ಗಮಿಸಲು '{quit_cmd}', ಹೆಸರನ್ನು ಆಯ್ಕೆಮಾಡಲು '{next_cmd}' ಎಂದು ಟೈಪ್ ಮಾಡಿ): ",
        "exiting_program": "ಕಾರ್ಯಕ್ರಮದಿಂದ ನಿರ್ಗಮಿಸಲಾಗುತ್ತಿದೆ.",
        "no_names_to_select": "ಆಯ್ಕೆಮಾಡಲು ಯಾವುದೇ ಹೆಸರುಗಳಿಲ್ಲ. ದಯವಿಟ್ಟು ಮೊದಲು ಕೆಲವು ಹೆಸರುಗಳನ್ನು ಸೇರಿಸಿ.",
        "name_added_to_list": "ಹೆಸರು '{name}' ಪಟ್ಟಿಗೆ ಸೇರಿಸಲಾಗಿದೆ.",
        "congratulations_winner": "ಅಭಿನಂದನೆಗಳು {name}! ನೀವು ವಿಜೇತರು!",
        "error_no_winner_provided": "ದೋಷ: ವಿಜೇತ ಕಾರ್ಯಕ್ಕೆ ಯಾವುದೇ ವಿಜೇತರನ್ನು ಒದಗಿಸಲಾಗಿಲ್ಲ.",
        "added_to_winners_list": "ಹೆಸರು '{name}' ವಿಜೇತರ ಪಟ್ಟಿಗೆ ಸೇರಿಸಲಾಗಿದೆ.",
        "game_over_all_selected": "ಆಟ ಮುಗಿದಿದೆ! ಎಲ್ಲಾ ಹೆಸರುಗಳನ್ನು ಆಯ್ಕೆಮಾಡಲಾಗಿದೆ. ವಿಜೇತರು: {winners_list}",
        "names_remaining": "ಆಯ್ಕೆಯ ಪೂಲ್‌ನಲ್ಲಿ {count} ಹೆಸರುಗಳು ಉಳಿದಿವೆ.",
        "quit_command": "ನಿರ್ಗಮಿಸು",
        "next_command": "ಮುಂದಿನದು"
    },
    "ml": { # Malayalam translations
        "select_language_prompt": "ഭാഷ തിരഞ്ഞെടുക്കുക (ഉദാ: en, es): ",
        "language_not_supported": "ഭാഷ '{lang}' പിന്തുണയ്ക്കുന്നില്ല. ഇംഗ്ലീഷ് ഉപയോഗിക്കുന്നു.",
        "enter_name_prompt": "നിങ്ങളുടെ പേര് ടൈപ്പ് ചെയ്യുക (അല്ലെങ്കിൽ പുറത്തുപോകാൻ '{quit_cmd}', ഒരു പേര് തിരഞ്ഞെടുക്കാൻ '{next_cmd}' എന്ന് ടൈപ്പ് ചെയ്യുക): ",
        "exiting_program": "പ്രോഗ്രാമിൽ നിന്ന് പുറത്തുകടക്കുന്നു.",
        "no_names_to_select": "തിരഞ്ഞെടുക്കാൻ പേരുകളൊന്നും ലഭ്യമല്ല. ദയവായി ആദ്യം കുറച്ച് പേരുകൾ ചേർക്കുക.",
        "name_added_to_list": "പേര് '{name}' ലിസ്റ്റിൽ ചേർത്തു.",
        "congratulations_winner": "അഭിനന്ദനങ്ങൾ {name}! നിങ്ങളാണ് വിജയി!",
        "error_no_winner_provided": "പിശക്: വിജയി ഫംഗ്ഷന് വിജയിയെ നൽകിയിട്ടില്ല.",
        "added_to_winners_list": "പേര് '{name}' വിജയികളുടെ ലിസ്റ്റിലേക്ക് ചേർത്തിട്ടുണ്ട്.",
        "game_over_all_selected": "കളി അവസാനിച്ചു! എല്ലാ പേരുകളും തിരഞ്ഞെടുത്തു. വിജയികൾ: {winners_list}",
        "names_remaining": "തിരഞ്ഞെടുപ്പ് പൂളിൽ {count} പേരുകൾ ശേഷിക്കുന്നു.",
        "quit_command": "പുറത്തുപോകുക",
        "next_command": "അടുത്തത്"
    },
    "ur": { # Urdu translations
        "select_language_prompt": "زبان منتخب کریں (مثلاً en, es): ",
        "language_not_supported": "زبان '{lang}' معاونت یافتہ نہیں ہے۔ انگریزی استعمال کی جا رہی ہے۔",
        "enter_name_prompt": "اپنا نام درج کریں (یا باہر نکلنے کے لیے '{quit_cmd}'، نام منتخب کرنے کے لیے '{next_cmd}' ٹائپ کریں): ",
        "exiting_program": "پروگرام سے باہر نکل رہے ہیں۔",
        "no_names_to_select": "منتخب کرنے کے لیے کوئی نام نہیں۔ براہ کرم پہلے کچھ نام شامل کریں۔",
        "name_added_to_list": "نام '{name}' فہرست میں شامل ہوگیا۔",
        "congratulations_winner": "مبارک ہو {name}! آپ فاتح ہیں!",
        "error_no_winner_provided": "خرابی: فاتح فنکشن کو کوئی فاتح فراہم نہیں کیا گیا۔",
        "added_to_winners_list": "نام '{name}' فاتحین کی فہرست میں شامل کر دیا گیا ہے۔",
        "game_over_all_selected": "کھیل ختم! تمام نام منتخب کر لیے گئے ہیں۔ فاتحین یہ ہیں: {winners_list}",
        "names_remaining": "انتخابی پول میں {count} نام باقی ہیں۔",
        "quit_command": "باہر نکلیں",
        "next_command": "اگلا"
    },
    "ga": { # Irish translations
        "select_language_prompt": "Roghnaigh teanga (e.g., en, es): ",
        "language_not_supported": "Ní thacaítear le teanga '{lang}'. Béarla in úsáid.",
        "enter_name_prompt": "Cuir isteach d'ainm (nó clóscríobh '{quit_cmd}' chun éirí as, '{next_cmd}' chun ainm a roghnú): ",
        "exiting_program": "Ag éirí as an gclár.",
        "no_names_to_select": "Níl aon ainmneacha le roghnú. Cuir roinnt ainmneacha leis ar dtús.",
        "name_added_to_list": "Cuireadh '{name}' leis an liosta.",
        "congratulations_winner": "Comhghairdeas {name}! Is tú an buaiteoir!",
        "error_no_winner_provided": "Earráid: Níor soláthraíodh aon bhuaiteoir don fheidhm buaiteora.",
        "added_to_winners_list": "Cuireadh '{name}' le liosta na mbuaiteoirí.",
        "game_over_all_selected": "Tá an cluiche thart! Roghnaíodh na hainmneacha go léir. Is iad na buaiteoirí: {winners_list}",
        "names_remaining": "Tá {count} ainm fágtha sa pholl roghnúcháin.",
        "quit_command": "éirigh as",
        "next_command": "seo chugainn"
    },
    "is": { # Icelandic translations
        "select_language_prompt": "Veldu tungumál (t.d. en, es): ",
        "language_not_supported": "Tungumál '{lang}' er ekki stutt. Nota enska.",
        "enter_name_prompt": "Sláðu inn nafnið þitt (eða '{quit_cmd}' til að hætta, '{next_cmd}' til að velja nafn): ",
        "exiting_program": "Hættir forriti.",
        "no_names_to_select": "Engin nöfn til að velja úr. Vinsamlegast bættu við nöfnum fyrst.",
        "name_added_to_list": "Nafninu '{name}' bætt við listann.",
        "congratulations_winner": "Til hamingju {name}! Þú ert sigurvegarinn!",
        "error_no_winner_provided": "Villa: Enginn sigurvegari var gefinn upp fyrir sigurvegarafallið.",
        "added_to_winners_list": "Nafninu '{name}' hefur verið bætt við lista sigurvegara.",
        "game_over_all_selected": "Leik lokið! Öll nöfn hafa verið valin. Sigurvegararnir eru: {winners_list}",
        "names_remaining": "Það eru {count} nöfn eftir í valpottinum.",
        "quit_command": "hætta",
        "next_command": "næsta"
    },
    "lv": { # Latvian translations
        "select_language_prompt": "Izvēlieties valodu (piemēram, en, es): ",
        "language_not_supported": "Valoda '{lang}' netiek atbalstīta. Tiek izmantota angļu valoda.",
        "enter_name_prompt": "Ievadiet savu vārdu (vai '{quit_cmd}', lai izietu, '{next_cmd}', lai izvēlētos vārdu): ",
        "exiting_program": "Iziet no programmas.",
        "no_names_to_select": "Nav vārdu, no kuriem izvēlēties. Lūdzu, vispirms pievienojiet dažus vārdus.",
        "name_added_to_list": "Vārds '{name}' pievienots sarakstam.",
        "congratulations_winner": "Apsveicam {name}! Jūs esat uzvarētājs!",
        "error_no_winner_provided": "Kļūda: Uzvarētāja funkcijai netika norādīts neviens uzvarētājs.",
        "added_to_winners_list": "Vārds '{name}' ir pievienots uzvarētāju sarakstam.",
        "game_over_all_selected": "Spēle beigusies! Visi vārdi ir atlasīti. Uzvarētāji ir: {winners_list}",
        "names_remaining": "Atlases kopā ir atlikuši {count} vārdi.",
        "quit_command": "iziet",
        "next_command": "nākamais"
    },
    "sk": { # Slovak translations
        "select_language_prompt": "Vyberte jazyk (napr. en, es): ",
        "language_not_supported": "Jazyk '{lang}' nie je podporovaný. Používa sa angličtina.",
        "enter_name_prompt": "Zadajte svoje meno (alebo '{quit_cmd}' pre ukončenie, '{next_cmd}' pre výber mena): ",
        "exiting_program": "Ukončuje sa program.",
        "no_names_to_select": "Nie sú k dispozícii žiadne mená na výber. Najprv pridajte nejaké mená.",
        "name_added_to_list": "Meno '{name}' bolo pridané do zoznamu.",
        "congratulations_winner": "Gratulujeme {name}! Ste víťaz!",
        "error_no_winner_provided": "Chyba: Funkcii víťaza nebol poskytnutý žiadny víťaz.",
        "added_to_winners_list": "Meno '{name}' bolo pridané do zoznamu víťazov.",
        "game_over_all_selected": "Hra sa skončila! Všetky mená boli vybrané. Víťazi sú: {winners_list}",
        "names_remaining": "V zozname na výber zostáva {count} mien.",
        "quit_command": "koniec",
        "next_command": "ďalší"
    },
    "hr": { # Croatian translations
        "select_language_prompt": "Odaberite jezik (npr. en, es): ",
        "language_not_supported": "Jezik '{lang}' nije podržan. Koristi se engleski.",
        "enter_name_prompt": "Unesite svoje ime (ili '{quit_cmd}' za izlaz, '{next_cmd}' za odabir imena): ",
        "exiting_program": "Izlaz iz programa.",
        "no_names_to_select": "Nema imena za odabir. Molimo prvo dodajte neka imena.",
        "name_added_to_list": "Ime '{name}' dodano na popis.",
        "congratulations_winner": "Čestitamo {name}! Vi ste pobjednik!",
        "error_no_winner_provided": "Greška: Pobjedničkoj funkciji nije dodijeljen pobjednik.",
        "added_to_winners_list": "Ime '{name}' dodano je na popis pobjednika.",
        "game_over_all_selected": "Igra je gotova! Sva imena su odabrana. Pobjednici su: {winners_list}",
        "names_remaining": "Preostalo je {count} imena u bazenu za odabir.",
        "quit_command": "izlaz",
        "next_command": "sljedeći"
    },
    "bg": { # Bulgarian translations
        "select_language_prompt": "Изберете език (напр. en, es): ",
        "language_not_supported": "Език '{lang}' не се поддържа. Използва се английски.",
        "enter_name_prompt": "Въведете вашето име (или '{quit_cmd}' за изход, '{next_cmd}' за избор на име): ",
        "exiting_program": "Излизане от програмата.",
        "no_names_to_select": "Няма имена за избор. Моля, първо добавете имена.",
        "name_added_to_list": "Име '{name}' е добавено към списъка.",
        "congratulations_winner": "Поздравления {name}! Вие сте победител!",
        "error_no_winner_provided": "Грешка: Не е предоставен победител на функцията за победител.",
        "added_to_winners_list": "Име '{name}' е добавено към списъка на победителите.",
        "game_over_all_selected": "Играта приключи! Всички имена са избрани. Победителите са: {winners_list}",
        "names_remaining": "Остават {count} имена в басейна за избор.",
        "quit_command": "изход",
        "next_command": "следващ"
    },
    "mt": { # Maltese translations
        "select_language_prompt": "Agħżel il-lingwa (eż. en, es): ",
        "language_not_supported": "Il-lingwa '{lang}' mhix appoġġjata. Qed tintuża l-Ingliż.",
        "enter_name_prompt": "Daħħal ismek (jew ittajpja '{quit_cmd}' biex toħroġ, '{next_cmd}' biex tagħżel isem): ",
        "exiting_program": "Ħiereġ mill-programm.",
        "no_names_to_select": "M'hemmx ismijiet minn fejn tagħżel. Jekk jogħġbok żid xi ismijiet l-ewwel.",
        "name_added_to_list": "L-isem '{name}' żdied mal-lista.",
        "congratulations_winner": "Prosit {name}! Inti r-rebbieħ!",
        "error_no_winner_provided": "Żball: L-ebda rebbieħ ma ngħata lill-funzjoni tar-rebbieħ.",
        "added_to_winners_list": "L-isem '{name}' żdied mal-lista tar-rebbieħa.",
        "game_over_all_selected": "Il-logħba spiċċat! L-ismijiet kollha ntgħażlu. Ir-rebbieħa huma: {winners_list}",
        "names_remaining": "Fadal {count} ismijiet fil-grupp tal-għażla.",
        "quit_command": "oħroġ",
        "next_command": "li jmiss"
    },
    "ja": { # Japanese translations
        "select_language_prompt": "言語を選択してください (例: en, es): ",
        "language_not_supported": "言語 '{lang}' はサポートされていません。英語を使用します。",
        "enter_name_prompt": "名前を入力してください (終了するには '{quit_cmd}'、名前を選択するには '{next_cmd}' と入力): ",
        "exiting_program": "プログラムを終了します。",
        "no_names_to_select": "選択できる名前がありません。まず名前を追加してください。",
        "name_added_to_list": "名前 '{name}' がリストに追加されました。",
        "congratulations_winner": "おめでとうございます {name} さん！あなたが勝者です！",
        "error_no_winner_provided": "エラー: 勝者関数に勝者が提供されませんでした。",
        "added_to_winners_list": "名前 '{name}' が勝者リストに追加されました。",
        "game_over_all_selected": "ゲーム終了！すべての名前が選択されました。勝者は次のとおりです: {winners_list}",
        "names_remaining": "選択プールには残り {count} 個の名前があります。",
        "quit_command": "終了",
        "next_command": "次へ"
    },
    "ko": { # Korean translations
        "select_language_prompt": "언어를 선택하세요 (예: en, es): ",
        "language_not_supported": "언어 '{lang}'는 지원되지 않습니다. 영어를 사용합니다.",
        "enter_name_prompt": "이름을 입력하세요 (종료하려면 '{quit_cmd}', 이름을 선택하려면 '{next_cmd}' 입력): ",
        "exiting_program": "프로그램을 종료합니다.",
        "no_names_to_select": "선택할 이름이 없습니다. 먼저 이름을 추가하세요.",
        "name_added_to_list": "이름 '{name}'이(가) 목록에 추가되었습니다.",
        "congratulations_winner": "축하합니다 {name}님! 당신이 승자입니다!",
        "error_no_winner_provided": "오류: 승자 함수에 승자가 제공되지 않았습니다.",
        "added_to_winners_list": "이름 '{name}'이(가) 승자 목록에 추가되었습니다.",
        "game_over_all_selected": "게임 종료! 모든 이름이 선택되었습니다. 승자는 다음과 같습니다: {winners_list}",
        "names_remaining": "선택 풀에 {count}개의 이름이 남아 있습니다.",
        "quit_command": "종료",
        "next_command": "다음"
    },
    "vi": { # Vietnamese translations
        "select_language_prompt": "Chọn ngôn ngữ (ví dụ: en, es): ",
        "language_not_supported": "Ngôn ngữ '{lang}' không được hỗ trợ. Sử dụng tiếng Anh.",
        "enter_name_prompt": "Nhập tên của bạn (hoặc gõ '{quit_cmd}' để thoát, '{next_cmd}' để chọn tên): ",
        "exiting_program": "Đang thoát chương trình.",
        "no_names_to_select": "Không có tên để chọn. Vui lòng thêm một số tên trước.",
        "name_added_to_list": "Tên '{name}' đã được thêm vào danh sách.",
        "congratulations_winner": "Chúc mừng {name}! Bạn là người chiến thắng!",
        "error_no_winner_provided": "Lỗi: Không có người chiến thắng nào được cung cấp cho hàm chiến thắng.",
        "added_to_winners_list": "Tên '{name}' đã được thêm vào danh sách những người chiến thắng.",
        "game_over_all_selected": "Trò chơi kết thúc! Tất cả các tên đã được chọn. Những người chiến thắng là: {winners_list}",
        "names_remaining": "Còn lại {count} tên trong nhóm lựa chọn.",
        "quit_command": "thoát",
        "next_command": "tiếp"
    },
    "th": { # Thai translations
        "select_language_prompt": "เลือกภาษา (เช่น en, es): ",
        "language_not_supported": "ไม่รองรับภาษา '{lang}' ใช้ภาษาอังกฤษ",
        "enter_name_prompt": "ป้อนชื่อของคุณ (หรือพิมพ์ '{quit_cmd}' เพื่อออก, '{next_cmd}' เพื่อเลือกชื่อ): ",
        "exiting_program": "กำลังออกจากโปรแกรม",
        "no_names_to_select": "ไม่มีชื่อให้เลือก โปรดเพิ่มชื่อก่อน",
        "name_added_to_list": "เพิ่มชื่อ '{name}' ในรายการแล้ว",
        "congratulations_winner": "ยินดีด้วย {name}! คุณคือผู้ชนะ!",
        "error_no_winner_provided": "ข้อผิดพลาด: ไม่มีการระบุผู้ชนะให้กับฟังก์ชันผู้ชนะ",
        "added_to_winners_list": "เพิ่มชื่อ '{name}' ในรายชื่อผู้ชนะแล้ว",
        "game_over_all_selected": "เกมจบแล้ว! เลือกชื่อทั้งหมดแล้ว ผู้ชนะคือ: {winners_list}",
        "names_remaining": "มีชื่อเหลืออยู่ {count} ชื่อในกลุ่มการเลือก",
        "quit_command": "ออก",
        "next_command": "ถัดไป"
    },
    "ms": { # Malay translations
        "select_language_prompt": "Pilih bahasa (cth: en, es): ",
        "language_not_supported": "Bahasa '{lang}' tidak disokong. Menggunakan Bahasa Inggeris.",
        "enter_name_prompt": "Masukkan nama anda (atau taip '{quit_cmd}' untuk keluar, '{next_cmd}' untuk memilih nama): ",
        "exiting_program": "Keluar dari program.",
        "no_names_to_select": "Tiada nama untuk dipilih. Sila tambah beberapa nama dahulu.",
        "name_added_to_list": "Nama '{name}' telah ditambah ke dalam senarai.",
        "congratulations_winner": "Tahniah {name}! Anda adalah pemenang!",
        "error_no_winner_provided": "Ralat: Tiada pemenang diberikan kepada fungsi pemenang.",
        "added_to_winners_list": "Nama '{name}' telah ditambah ke senarai pemenang.",
        "game_over_all_selected": "Permainan tamat! Semua nama telah dipilih. Pemenangnya ialah: {winners_list}",
        "names_remaining": "Terdapat {count} nama yang tinggal dalam kumpulan pemilihan.",
        "quit_command": "keluar",
        "next_command": "seterusnya"
    },
    "fil": { # Filipino translations
        "select_language_prompt": "Pumili ng wika (hal. en, es): ",
        "language_not_supported": "Hindi suportado ang wikang '{lang}'. Ingles ang gagamitin.",
        "enter_name_prompt": "Ilagay ang iyong pangalan (o i-type ang '{quit_cmd}' para lumabas, '{next_cmd}' para pumili ng pangalan): ",
        "exiting_program": "Lumalabas sa programa.",
        "no_names_to_select": "Walang mga pangalan na mapagpipilian. Mangyaring magdagdag muna ng ilang pangalan.",
        "name_added_to_list": "Idinagdag ang '{name}' sa listahan.",
        "congratulations_winner": "Binabati kita {name}! Ikaw ang nagwagi!",
        "error_no_winner_provided": "Error: Walang nagwagi na ibinigay sa function ng nagwagi.",
        "added_to_winners_list": "Idinagdag si '{name}' sa listahan ng mga nagwagi.",
        "game_over_all_selected": "Tapos na ang laro! Napili na ang lahat ng pangalan. Ang mga nagwagi ay: {winners_list}",
        "names_remaining": "May natitirang {count} pangalan sa selection pool.",
        "quit_command": "labas",
        "next_command": "susunod"
    },
    "tr": { # Turkish translations
        "select_language_prompt": "Dil seçin (örn: en, es): ",
        "language_not_supported": "Dil '{lang}' desteklenmiyor. İngilizce kullanılıyor.",
        "enter_name_prompt": "Adınızı girin (veya çıkmak için '{quit_cmd}', bir ad seçmek için '{next_cmd}' yazın): ",
        "exiting_program": "Programdan çıkılıyor.",
        "no_names_to_select": "Seçilecek ad yok. Lütfen önce birkaç ad ekleyin.",
        "name_added_to_list": "Ad '{name}' listeye eklendi.",
        "congratulations_winner": "Tebrikler {name}! Kazanan sizsiniz!",
        "error_no_winner_provided": "Hata: Kazanan işlevine kazanan sağlanmadı.",
        "added_to_winners_list": "Ad '{name}' kazananlar listesine eklendi.",
        "game_over_all_selected": "Oyun bitti! Tüm adlar seçildi. Kazananlar: {winners_list}",
        "names_remaining": "Seçim havuzunda {count} ad kaldı.",
        "quit_command": "çık",
        "next_command": "sonraki"
    },
    "fa": { # Persian translations
        "select_language_prompt": "زبان را انتخاب کنید (مثال: en, es): ",
        "language_not_supported": "زبان '{lang}' پشتیبانی نمی‌شود. از انگلیسی استفاده می‌شود.",
        "enter_name_prompt": "نام خود را وارد کنید (یا برای خروج '{quit_cmd}'، برای انتخاب نام '{next_cmd}' را تایپ کنید): ",
        "exiting_program": "در حال خروج از برنامه.",
        "no_names_to_select": "هیچ نامی برای انتخاب وجود ندارد. لطفاً ابتدا چند نام اضافه کنید.",
        "name_added_to_list": "نام '{name}' به لیست اضافه شد.",
        "congratulations_winner": "تبریک {name}! شما برنده شدید!",
        "error_no_winner_provided": "خطا: هیچ برنده‌ای به تابع برنده ارائه نشده است.",
        "added_to_winners_list": "نام '{name}' به لیست برندگان اضافه شده است.",
        "game_over_all_selected": "بازی تمام شد! همه نام‌ها انتخاب شدند. برندگان عبارتند از: {winners_list}",
        "names_remaining": "{count} نام در استخر انتخاب باقی مانده است.",
        "quit_command": "خروج",
        "next_command": "بعدی"
    },
    "he": { # Hebrew translations
        "select_language_prompt": "בחר שפה (לדוגמה: en, es): ",
        "language_not_supported": "השפה '{lang}' אינה נתמכת. נעשה שימוש באנגלית.",
        "enter_name_prompt": "הקלד את שמך (או '{quit_cmd}' ליציאה, '{next_cmd}' לבחירת שם): ",
        "exiting_program": "יוצא מהתוכנית.",
        "no_names_to_select": "אין שמות לבחירה. אנא הוסף כמה שמות תחילה.",
        "name_added_to_list": "השם '{name}' הוסף לרשימה.",
        "congratulations_winner": "מזל טוב {name}! אתה המנצח!",
        "error_no_winner_provided": "שגיאה: לא סופק מנצח לפונקציית המנצח.",
        "added_to_winners_list": "השם '{name}' הוסף לרשימת המנצחים.",
        "game_over_all_selected": "המשחק הסתיים! כל השמות נבחרו. המנצחים הם: {winners_list}",
        "names_remaining": "נותרו {count} שמות במאגר הבחירה.",
        "quit_command": "יציאה",
        "next_command": "הבא"
    }
}

current_language = "en" 

def get_message(key, **kwargs):
    """Retrieves a translated message string for the current language."""
    global current_language
    
    message_template = translations.get(current_language, translations["en"]).get(key, translations["en"].get(key))
    if message_template is None:
        
        return key 
    return message_template.format(**kwargs)

def set_language():
    """Allows the user to select a language."""
    global current_language
   
    lang_code = input(translations["en"]["select_language_prompt"]).strip().lower()
    if lang_code in translations:
        current_language = lang_code
    else:
   
        print(translations["en"]["language_not_supported"].format(lang=lang_code))
        current_language = "en" 

def main(names_list):
    while True:
        name_input = input(get_message("enter_name_prompt", quit_cmd=get_message("quit_command"), next_cmd=get_message("next_command")))
        if name_input.lower() == get_message("quit_command"):
            print(get_message("exiting_program"))
            break
        elif name_input.lower() == get_message("next_command"):
            if not names_list:
                print(get_message("no_names_to_select"))
            else:
                selected_winner_name = make_selection(names_list)
                if selected_winner_name:
                    winner(selected_winner_name)
        else:
            names_list.append(name_input)
            print(get_message("name_added_to_list", name=name_input))

def make_selection(current_names):
    if not current_names:
        print(get_message("no_names_to_select"))
        return None
    
    selected_name = random.choice(current_names)
    print(get_message("congratulations_winner", name=selected_name))
    current_names.remove(selected_name)
    return selected_name

def winner(name_of_the_winner):
    if name_of_the_winner is None:
        print(get_message("error_no_winner_provided"))
        return

    winners.append(name_of_the_winner)
    print(get_message("added_to_winners_list", name=name_of_the_winner))

    if not names: # Check the global names list
        print(get_message("game_over_all_selected", winners_list=winners))
    else:
        print(get_message("names_remaining", count=len(names)))

if __name__ == "__main__":
    set_language() # Call set_language at the beginning
    main(names)
