"""
wsgi.py
- launch for production env
"""

from triffidsapi.app import create_app
application = create_app()
