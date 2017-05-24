from auth_service import AuthService

if __name__ == '__main__':
    app = AuthService(use_db=True)
    app.instance.logger.info(app.instance.config['SQLALCHEMY_DATABASE_URI'])
    app.instance.run(debug=True, port=5001)
