"""
server.py
- this is the starting point for the app
"""

if __name__ == '__main__':
    from triffidsapi.app import create_app
    app = create_app()
    app.run(debug=True)
