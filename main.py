import sys
from action_handler import addAction

action: str = sys.argv[1]

match action:
    case 'add':
        addAction(description=sys.argv[2])