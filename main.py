import sys
from action_handler import addAction, updateAction, deleteAction, updateStatus, listAction, listByStatus

action: str = sys.argv[1]

match action:
    case 'add': addAction(descriptions=sys.argv[2:])
    case 'update': updateAction(id=int(sys.argv[2]),description=sys.argv[3])
    case 'mark-in-progress': updateStatus(ids=sys.argv[2:], status='in-progress')
    case 'mark-todo': updateStatus(ids=sys.argv[2:], status='todo')
    case 'mark-done': updateStatus(ids=sys.argv[2:], status='done')
    case 'delete': deleteAction(ids=sys.argv[2:])
    case 'list': 
        if len(sys.argv) > 2: listByStatus(status=sys.argv[2])
        else: listAction()