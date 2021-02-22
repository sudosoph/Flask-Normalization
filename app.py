from flask import Flask, request
from pydub import AudioSegment
app = Flask(__name__)

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

@app.route("/")
def index():
    return 'Index Page'

@app.route("/normalize", methods=['POST'])    
def normalize():
    if request.method == 'POST':
        sound = AudioSegment.from_file("test.wav", "wav")
        normalized_sound = match_target_amplitude(sound, -20.0)
        normalized_sound.export("normalized_test.wav", format="wav")
    return 'Normalization script'

if  __name__ == "__main__":
    app.run()

