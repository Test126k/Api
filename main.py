from fastapi import FastAPI, Query
import httpx

app = FastAPI()

RAPID_API_HOST = "terabox-downloader-direct-download-link-generator2.p.rapidapi.com"
RAPID_API_KEY = "99a09605bfmshdf6a54791a55dd3p1a24f5jsn4ff83a6487ae"

@app.get("/")
def home():
    return {"status": "ok", "message": "TeraBox API is running"}

@app.get("/terabox")
async def get_direct_link(url: str = Query(..., alias="file_url")):
    headers = {
        "x-rapidapi-host": RAPID_API_HOST,
        "x-rapidapi-key": RAPID_API_KEY
    }

    query_url = f"https://{RAPID_API_HOST}/url?url={url}"

    async with httpx.AsyncClient() as client:
        response = await client.get(query_url, headers=headers)

    try:
        return response.json()
    except Exception as e:
        return {"error": "Invalid response", "detail": str(e)}
