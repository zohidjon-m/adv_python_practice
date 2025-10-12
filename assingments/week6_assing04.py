# Assignment 4: Interactive list builder (no functions, no error handling).
# Commands: add <item>, remove <item>, show, done
items = []
print("Commands: add <item>, remove <item>, show, done")
while True:
    raw = input("> ").strip()
    if not raw:
        continue
    parts = raw.split()
    cmd = parts[0].lower()
    arg = " ".join(parts[1:]) if len(parts) > 1 else ""

    if cmd == "add":
        if not arg:
            print("Specify an item to add.")
            continue
        items.append(arg)
    elif cmd == "remove":
        if not arg:
            print("Specify an item to remove.")
            continue
        if arg in items:
            items.remove(arg)
        else:
            print(f"'{arg}' not in list; nothing removed.")
    elif cmd == "show":
        print(f"Current list: {items}")
    elif cmd == "done":
        break
    else:
        print("Unknown command. Use: add, remove, show, done")

print(f"Final list: {items}")
print(f"Length: {len(items)}")
print(f"Sorted copy: {sorted(items)}")
