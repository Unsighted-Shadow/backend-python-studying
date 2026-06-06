from flask import Flask

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def server_status():

    return {
        "server": "Flask",
        "status": "active",
        "message": "Welcome to my Flask Portfolio API!"
    }
        
if __name__ == '__main__':
    app.run(debug=True)
