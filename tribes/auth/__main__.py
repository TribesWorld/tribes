from auth_service import AuthService

if __name__ == '__main__':
    app = AuthService()
    app.instance.run(debug=True, port=5001)
