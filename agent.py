import csv

def load_tree(file):
    tree = {}
    children = {}

    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            tree[row['id']] = row
            parent = row['parentId']
            if parent:
                children.setdefault(parent, []).append(row['id'])

    return tree, children


def update_signal(signal, state):
    if signal:
        for s in signal.split(';'):
            if ':' in s:
                axis, value = s.split(':')
                state.setdefault(axis, {})
                state[axis][value] = state[axis].get(value, 0) + 1


def dominant(state, axis):
    if axis not in state:
        return "unknown"
    return max(state[axis], key=state[axis].get)


def replace_text(text, answers, state):
    for k, v in answers.items():
        text = text.replace(f"{{{k}.answer}}", v)

    text = text.replace("{axis1.dominant}", dominant(state, "axis1"))
    text = text.replace("{axis2.dominant}", dominant(state, "axis2"))
    text = text.replace("{axis3.dominant}", dominant(state, "axis3"))

    return text


def run():
    tree, children = load_tree("reflection-tree.tsv")

    current = "START"
    answers = {}
    state = {}

    while current:
        node = tree[current]
        text = replace_text(node['text'], answers, state)

        print("\n" + text)

        update_signal(node.get('signal', ''), state)

        # QUESTION
        if node['type'] == "question":
            options = node['options'].split('|')

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose option: ")) - 1
            answers[current] = options[choice]

            current = children[current][0]

        # DECISION
        elif node['type'] == "decision":
            rules = node['options'].split(';')
            last = list(answers.values())[-1]

            for rule in rules:
                cond, target = rule.split(':')
                values = cond.replace("answer=", "").split('|')

                if last in values:
                    current = target
                    break

        # AUTO NODES
        elif node['type'] in ["reflection", "bridge", "start"]:
            current = children.get(current, [None])[0]

        # SUMMARY
        elif node['type'] == "summary":
            print("\n--- SUMMARY ---")
            print(text)
            break

        elif node['type'] == "end":
            break


if __name__ == "__main__":
    run()
