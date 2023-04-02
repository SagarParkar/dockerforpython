from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
import whisper
import logging
import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
id = 123456789
audio_file = f"{id}.mp3"
model = whisper.load_model("base", "cpu")
logging.debug("Model loaded")
transcription = ""

async def transcribe_audio(audio_file: str) -> str:
    result = model.transcribe(audio_file)
    return result["text"]


@app.get("/")
async def read_root(request: Request):
    logging.debug("Getting transcription")

    logging.debug(f"Transcription started at {datetime.datetime.now()}")
    transcription = await transcribe_audio(audio_file)
    logging.debug(f"Transcription finished at {datetime.datetime.now()}")

    with open(f"{id}.txt", "w") as f:
        f.write(transcription)
    logging.debug("Transcription saved")

    return templates.TemplateResponse("index.html", {
        "request": request,  
        "transcription": transcription
        })


