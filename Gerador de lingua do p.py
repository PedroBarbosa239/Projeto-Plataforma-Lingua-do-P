from hyphen import Hyphenator
import sounddevice as sd
import vosk
import queue
import json


def lingua_p(frase):
    h = Hyphenator('pt_BR')  
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        silabas = h.syllables(palavra)

        if silabas:
            palavra_modificada = ' '.join(['P' + s for s in silabas])
        else:
            palavra_modificada = 'P' + palavra

        resultado.append(palavra_modificada)

    return ' '.join(resultado)



model = vosk.Model("vosk-model-small-pt-0.3")
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))


with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("🎙️ Fale algo... (Ctrl+C para sair)")
    rec = vosk.KaldiRecognizer(model, 16000)

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            frase = result['text']
            if frase:
                print("🗣️ Frase final:     ", frase)
                print("🌀 Língua do P:     ", lingua_p(frase))
        else:
            partial = json.loads(rec.PartialResult())
            frase_parcial = partial.get("partial", "")
            if frase_parcial:
                print("🔹 Parcial:         ", frase_parcial, end='\r')

