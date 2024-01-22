import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.getg("PORT")),
        debug=os.environ.get("DEBUG"),
    )