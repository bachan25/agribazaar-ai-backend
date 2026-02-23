from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.send_email_controller import router as email_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
            title="AgriBazaar AI FastAPIs",
            description="APIs for AgriBazaar AI services",
            version="1.0.0",
            docs_url="/api/docs",
            redoc_url="/api/redoc",
            openapi_url="/api/openapi.json"
            )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email_router, prefix="/api/email", tags=["Email Service"])
