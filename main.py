import whisper

#Load AI engine Model Size Medimum [ Spec's and efficieny of each engine size can be viewed on OpenAI site]. 
model = whisper.load_model("medium")

# load audio and pad/trim it to fit 30 seconds for POC uze. 
audio = whisper.load_audio("data/Yonathan.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decodes the audio pattern to language 
options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

# print the recognized language translation into a text file
if __name__ == "__main__":
    print(result.text)
