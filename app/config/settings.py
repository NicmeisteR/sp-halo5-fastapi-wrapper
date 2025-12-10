# Configuration for Halo 5 API
import os
if not os.environ.get("AWS_EXECUTION_ENV"):
	try:
		from dotenv import load_dotenv
		load_dotenv()
	except ImportError:
		pass
HALO_API_KEY = os.getenv("HALO_API_KEY", "")
HALO_API_BASE_URL = "https://www.haloapi.com"
