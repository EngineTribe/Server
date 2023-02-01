from config import STORAGE_URL, STORAGE_AUTH_KEY, STORAGE_PROXIED, STORAGE_PROVIDER
from database.db import Database
from session.db import SessionDatabase
from storage_provider import StorageProviderOneDriveCF, StorageProviderOneManager, StorageProviderDatabase

db: Database = Database()

connection_count: int = 0

match STORAGE_PROVIDER:
    case "onedrive-cf":
        storage: StorageProviderOneDriveCF = StorageProviderOneDriveCF(
            url=STORAGE_URL, auth_key=STORAGE_AUTH_KEY, proxied=STORAGE_PROXIED
        )
    case "onemanager":
        storage: StorageProviderOneManager = StorageProviderOneManager(
            url=STORAGE_URL, admin_password=STORAGE_AUTH_KEY
        )
    case "database":
        storage: StorageProviderDatabase = StorageProviderDatabase(
            base_url=STORAGE_URL,
            database=db
        )

session_db: SessionDatabase = SessionDatabase()
