# write your code here
commands = "plain bold italic header link inline-code new-line ordered-list unordered-list"
special_commands = "!help !done"
markdown = ""


def get_help():
    print("Available formatters:", commands)
    print("Special commands:", special_commands)


def done():
    with open("output.md", "w") as file:
        file.write(markdown)
        file.close()


def get_formatter(formatter):
    if formatter == "plain":
        return plain_formatter(input("Text: "))
    elif formatter == "bold":
        return bold_formatter(input("Text: "))
    elif formatter == "italic":
        return italic_formatter(input("Text: "))
    elif formatter == "inline-code":
        return inline_code(input("Text: "))
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        return link_formatter(label, url)
    elif formatter == "header":
        while True:
            level = int(input("Level: "))
            if level in range(1, 7):
                return header_formatter(level, input("Text: "))
            else:
                print("The level should be within the range of 1 to 6")
    elif formatter == "new-line":
        return new_line()
    elif formatter == "ordered-list" or "unordered-list":
        return list_formatter(formatter)


def plain_formatter(text):
    return text


def bold_formatter(text):
    return "**{}**".format(text)


def italic_formatter(text):
    return "*{}*".format(text)


def inline_code(text):
    return "`{}`".format(text)


def new_line():
    return "\n"


def link_formatter(label, url):
    return f"[{label}]({url})"


def header_formatter(level, text):
    header_level = "#" * int(level)
    return f"{header_level} {text}\n"


def list_formatter(formatter):
    items_list = ""
    while True:
        rows = int(input("Number of rows:"))
        if rows < 1:
            print("The number of rows should be greater than zero")
        else:
            break

    for i in range(1, rows + 1):
        item = input(f"Row #{i}: ")
        if formatter == "ordered-list":
            items_list += f"{i}. {item}\n"
        else:
            items_list += f"* {item}\n"
    return items_list


def start_markdown():

    while True:
        global markdown
        command = input("Choose a formatter: ")
        if command == "!done":
            done()
            break
        elif command in commands:
            markdown += get_formatter(command)
            print(markdown)
        elif command == "!help":
            get_help()
        else:
            print("Unknown formatting type or command")


start_markdown()
