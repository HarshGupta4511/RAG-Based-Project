import whisper
import json
model = whisper.load_model("base")
result = model.transcribe(audio = "audios/sample.mp3" 
                        , language = "Hindi"
                        , task = "Translate"
                        , word_timestamps = "False" )
print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({ "start":segment['start'] , "end":segment['end'] , "text":segment['text']})


with open("output.json" ,"w") as f:
    json.dump(chunks,f)