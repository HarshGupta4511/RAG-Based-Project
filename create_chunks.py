import whisper
import json
import os

audios = os.listdir("audios")
model = whisper.load_model("base")

for audio in audios:
    if ("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number , title)  
        result = model.transcribe(audio = f"audios/{audio}"
                                         , language = "Hindi"
                                         , task = "Translate"
                                         , word_timestamps = "False" )
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number":number, "start":segment['start'] , "end":segment['end'] , "text":segment['text']})

        chunks_with_metadata = {"chunks":chunks , "text":result['text']}
    with open(f"jsons/{audio}.json" ,"w") as f:
        json.dump(chunks_with_metadata,f)
