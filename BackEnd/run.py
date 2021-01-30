# If we want to use app package which we create earlier , need to import it 
from app import app


if __name__ == "__main__":
    app.run(debug=True)

