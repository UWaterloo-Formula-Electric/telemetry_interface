"""
Common application variables
"""

import os

# Core
TCP_HOST: str = os.environ.get('SERVER_IP')
TCP_PORT: int = os.environ.get('SERVER_PORT')