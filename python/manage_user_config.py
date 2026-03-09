def add_setting(settings, config):
    key, value = config[0].lower(), config[1].lower()

    if key in settings.keys():
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    else:
        settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, config):
    key, value = config[0].lower(), config[1].lower()

    if key in settings.keys():
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings.keys():
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    if settings == {}:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.lower().capitalize()}: {value}\n"

    return output


test_settings = {"theme": "light", "notifications": "enabled", "volume": "high"}
print(add_setting({"theme": "light"}, ("THEME", "dark")))
print(add_setting({"theme": "light"}, ("volume", "high")))
print(update_setting({"theme": "light"}, ("theme", "dark")))
print(update_setting({"theme": "light"}, ("volume", "high")))
print(delete_setting({"theme": "light"}, "theme"))
print(view_settings(test_settings))
