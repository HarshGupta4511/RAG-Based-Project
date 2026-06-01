# How to use the AI teaching assistant on your own data
## Step1 - Collect your videos
Move all your videos files to the videos folder 
-- i have downloaded the videos from the youtube by using bgmf3 and all videos credits goes to Rishabh Sir's Python Course!!

## Step2 - Convert it into mp3 (Audio)
Convert all the videos files to mp3 by running video_to_text

## Step3 - Convert mp3 to json 
Convert all the mp3 files to json by running audio_to_text    
-- i have less storage and not powerfull pc that's why i only convert 7 mp3 to json and it take lots of time and cpu storage to do so because i was using wishper.

-- if you have money then by the open ai api to convert and into json.

## Step4 - Convert the json files to vectors
use the file read_chunks.py to do so and then later save it by using joblib as i do earlier.

## Step5 - Prompt Generation and Feeding to LLM
Read the joblib file and load it itno the memory. Then create a relevant prompt as per the user query and feed it to the LLM 

-- Choosing a right model is also necessary i have used llama 3.2 which is really fast but not efficient in text generation like it donesnt give that good response instead of it use GPT-4 or 5 you will get good response.