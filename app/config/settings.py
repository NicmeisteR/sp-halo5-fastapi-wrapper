# Configuration for Halo 5 API
from dotenv import load_dotenv
load_dotenv()
import os
HALO_API_KEY = os.getenv("HALO_API_KEY", "")
HALO_API_BASE_URL = "https://www.haloapi.com"
