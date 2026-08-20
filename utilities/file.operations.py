def write_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

    return "Data saved successfully."


def append_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

    return "Data added successfully."


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."


def update_file(filename, old_text, new_text):
    try:
        with open(filename, "r") as file:
            data = file.read()

        data = data.replace(old_text, new_text)

        with open(filename, "w") as file:
            file.write(data)

        return "File updated successfully."

    except FileNotFoundError:
        return "File not found."
    
