from service import Service

if __name__ == '__main__':
    app = Service(user_db=True)
    app.instance.run(debug=True, port=5000)
