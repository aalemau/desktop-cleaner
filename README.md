Desktop Cleaner

Descrizione:
-Desktop Cleaner è una piccola applicazione Python che pulisce la cartella temporanea del sistema operativo Windows rimuovendo file e cartelle inutili. L’interfaccia grafica semplice permette di avviare la pulizia con un clic. Usa questo tool con cautela, la pulizia rimuove tutti i file nella cartella temporanea, inclusi quelli eventualmente in uso.

Funzionalità:
-Elimina tutti i file e le cartelle dalla directory temporanea del sistema.
-Interfaccia grafica con un pulsante di facile utilizzo.
-Compatibile con Windows.

Requisiti:
-Python 3.10+
-Modulo tkinter (incluso nella maggior parte delle installazioni Python standard)

Come creare l'eseguibile
Per creare un file .exe per Windows:
-Installa PyInstaller (se non lo hai già):
-pip install pyinstaller
 Da terminale, nella cartella del progetto, esegui:
-pyinstaller --onefile cleaner.py
 Il file eseguibile sarà creato nella cartella dist.

Come usare:
-Clona o scarica questo repository.

-Apri il terminale e vai nella cartella del progetto.

-Esegui lo script con:
    python cleaner.py

-Clicca su "Pulisci" per avviare la pulizia.

Licenza
Questo progetto è open source e libero da usare.