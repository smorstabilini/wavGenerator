# creare l'ambiente virtuale
> python3 -m venv testserver

# attivare l'ambiente virtuale
> ./bin/activate

# Una volta attivo l'ambiente virtuale, installare le dipendenze:
> pip3 install -r requirements.txt


Utilizzo:

> python generaWav.py "nome cognome" ~/mydir/checkName



-----   work in progress, non prendere alla lettera quanto scritto qua sotto:


http://localhost/startTest?guid=xxx&step=yyy&additionalData=zzz

guid è obbligatorio
step e additionalData sono facoltativi


# per testare più casi in una volta sola:
http://localhost/startTestSuite?suiteId=xyz


# per testare tutto:
http://localhost/startAllTests




# riferimenti:
https://pythonprogramminglanguage.com/text-to-speech/

# cherrypy (server web):
https://cherrypy.org/



Installazione di ffmpeg per permettere la conversione da mp3 a wav:
# brew install ffmpeg
