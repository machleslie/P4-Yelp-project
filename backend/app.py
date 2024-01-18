from __init__ import app


if __name__ == '__main__':
    from flask_migrate import upgrade
    with app.app_context():
        upgrade()
    app.run(debug=True, port=5555)
