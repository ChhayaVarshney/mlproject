import os
from application import application  # Import your Flask app

if __name__ == "__main__":
    # Get port from environment (Elastic Beanstalk sets $PORT), fallback to 8080
    port = int(os.environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port)
