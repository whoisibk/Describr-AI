from dotenv import load_dotenv
from google import genai
import cv2 as cv
import base64
import httpx, sys, os

load_dotenv() # load environment vars from the env file

prompt_ = "Give a brief but comprehensive description of the image. Not beyond 4 lines."
def apicall(fp, prompt=prompt_) -> str:
    img = cv.imread(fp)
    if img is None:
        print("Failed to load image")
        return
    ext = os.path.splitext(fp)  # splitting the file name from its extension
    success, encoded_img = cv.imencode(ext[1].lower(), img)
    if success:
        open_api_img = base64.b64encode(encoded_img).decode("utf-8")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    if GEMINI_API_KEY:
        client = genai.Client(api_key=GEMINI_API_KEY)

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/png", "data": open_api_img}},
                ],
            )

            return response.text
        except httpx.ConnectError:
            sys.exit("Internet connection was interrupted")
    else:
        sys.exit("Provide a valid Gemini API Key")


if __name__ == "__main__":
    apicall()