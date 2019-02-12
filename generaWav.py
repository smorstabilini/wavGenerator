from gtts import gTTS 
import sys
from pydub import AudioSegment

# chiamare questo scirpt come 
# python3 generaWav "stringa da vocalizzare" "nome file di output.waw"

# The text that you want to convert to audio 
if len(sys.argv) != 3:
    print ("Parametri non validi\n")
    for i in range(len(sys.argv)):
        print("Parametro {}: {}".format(i, sys.argv[i]))
    print("\n")
    print("Esempio di utilizzo: python3 generaWaw.py \"stringa da vocalizzare\" \"nomefile senza estensione\"\n")
else:
    mytext = sys.argv[1]

    # Language in which you want to convert 
    language = 'it'
    temp_name = "{}.mp3".format(sys.argv[2])
    out_name = "{}.wav".format(sys.argv[2])

    # Passing the text and language to the engine
    tts = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a wav file named sample
    # tts.save(sys.argv[2])
    tts.save(temp_name)

    sound = AudioSegment.from_mp3(temp_name)
    sound.export(out_name, format="wav")

print("Fine script.\n")
