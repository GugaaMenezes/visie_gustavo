import os
from app import app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5003))
    app.run(debug=True)
