import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # You can change the number 5000 to any port you prefer
    # The 'int(os.environ.get("PORT", 5000))' means: 
    # Use the PORT environment variable if it exists, otherwise use 5000.
    port = int(os.environ.get("PORT", 5000))  
    
    app.run(host="0.0.0.0", port=port, debug=True)