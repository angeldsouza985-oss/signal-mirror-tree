import csv

def load_tree(file):
    tree = {}
    children_map = {}

    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            tree[row['id']] = row
            parent = row['parentId']
            if parent:
                children_map.setdefault(parent, []).append(row['id'])

    return tree, children_map


def update_signals(signal_str, state):
    if signal_str:
        for s in signal_str.split(';'):
            if ':' in s:
                axis, value = s.split(':')
                state.setdefault(axis, {})
                state[axis][value] = state[axis].get(value, 0) + 1


def get_dominant(state, axis):
    if axis not in state:
        return "unknown"
    return max(state[axis], key=state[axis].get)


def interpolate(text, answers, state):
    # replace answers
    for k, v in answers.items():
        text = text.replace(f"{{{k}.answer}}", v)

    # replace axis summary
    text = text.replace("{axis1.dominant}", get_dominant(state, "control"))
    text = text.replace("{axis2.dominant}", get_dominant(state, "value"))
    text = text.replace("{axis3.dominant}", get_dominant(state, "impact"))

    return text


def run():
    tree, children_map = load_tree("reflection-tree.tsv")

    current = "START"
    answers = {}
    state = {}

    while current:
        node = tree[current]
        node_type = node['type']
        text = interpolate(node['text'], answers, state)

        print("\n" + text)

        update_signals(node.get('signal', ''), state)

        # QUESTION
        if node_type == "question":
            options = node['options'].split('|')

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose option: ")) - 1
            answer = options[choice]

            answers[current] = answer

            # go to child
            current = children_map[current][0]

        # DECISION
        elif node_type == "decision":
            rules = node['options'].split(';')
            last_answer = list(answers.values())[-1]

            for rule in rules:
                cond, target = rule.split(':')
                cond_vals = cond.replace("answer=", "").split('|')

                if last_answer in cond_vals:
                    current = target
                    break

        # AUTO NODES
        elif node_type in ["reflection", "bridge", "start"]:
            current = children_map.get(current, [None])[0]

        # SUMMARY
        elif node_type == "summary":
            print("\n--- SUMMARY ---")
            print(text)
            break

        elif node_type == "end":
            break


if __name__ == "__main__":
    run()
