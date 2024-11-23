n = int(input())
action_shortcuts = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

possible_actions = {}
for _ in range(n):
    input_data = input().split()
    file_name, actions = input_data[0], input_data[1:]
    possible_actions[file_name] = actions

m = int(input())

for _ in range(m):
    action, file_name = input().split()
    action_short = action_shortcuts.get(action.lower(), '')
    if file_name in possible_actions and action_short in possible_actions[file_name]:
        print('OK')
    else:
        print('Access denied')





