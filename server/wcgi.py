"""
wsgi.py
- launch for production env
"""

from triffidsapi.app import create_app
app = create_app()
