HOST = 'enginetribe.gq'  # Engine Tribe Central Server
PORT = 25019  # Default port that SMM_WE uses

DB_TYPE = 'mysql'  # Only MySQL is supported now
DB_HOST = 'localhost'  # MySQL host
DB_PORT = 3306  # MySQL port
DB_USER = 'enginetribe'  # MySQL user (not UNIX user)
DB_PASS = 'enginetribe'  # MySQL password (not UNIX password)
DB_NAME = 'enginetribe'  # MySQL database name

STORAGE_BACKEND = 'onedrive-cf-index'  # Only onedrive-cf-index is supported now
# https://github.com/spencerwooo/onedrive-cf-index
STORAGE_URL = 'http://storage.enginetribe.yidaozhan.top/'  # onedrive-cf-index instance url
STORAGE_AUTH_KEY = 'enginetribesA7EKiqBxY6QeH'  # onedrive-cf-index Auth Key
STORAGE_PROXIED = True  # Proxy levels via CloudFlare CDN
