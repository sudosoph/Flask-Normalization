from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

sound = AudioSegment.from_file("test.wav", "wav")
normalized_sound = match_target_amplitude(sound, -20.0)
normalized_sound.export("normalized_test.wav", format="wav")