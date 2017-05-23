from service import Service

if __name__ == '__main__':
    app = Service()
    app.instance.run(debug=True, port=5000)
