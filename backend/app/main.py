from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base

# डेटाबेस टेबल्स बनाना (यदि पहले से नहीं बनी हैं)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="The Cakery House API", version="1.0")

# CORS Setup: ताकि Astro (Frontend) बिना किसी एरर के बैकएंड से डेटा ला सके
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # डेवलपमेंट के लिए सभी ओरिजिन अलाउड हैं
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to The Cakery House Backend API!"}

# नोट: आगे हम यहाँ अपने Routers (auth, products, orders) को शामिल (include) करेंगे।