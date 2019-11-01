def sanitise(item):
    """
    Works through a given object and removes dictionary attributes which have None Type or empty string values
    :param item: Object to sanitise
    :return: Sanitised object
    """
    item_to_sanitise = item.copy()
    if isinstance(item_to_sanitise, dict):
        item_to_sanitise = _sanitise_dictionary(item_to_sanitise)
    elif isinstance(item_to_sanitise, (list, str)):
        if len(item_to_sanitise) == 0:
            return None
        elif isinstance(item_to_sanitise, list):
            return _sanitise_list(item_to_sanitise)

    return item_to_sanitise


def _sanitise_dictionary(item):
    # We must copy this object as we will iterate through it but may remove nodes from it
    item_to_sanitise = item.copy()
    for key, value in item.items():
        # If the key is a dictionary then pass the value back into this method again
        if isinstance(value, dict):
            if len(item_to_sanitise[key]) == 0:
                del item_to_sanitise[key]
            else:
                sanitised_key = sanitise(value)

                if sanitised_key is None:
                    del item_to_sanitise[key]
                else:
                    item_to_sanitise[key] = sanitised_key

        elif value is None or value == "":
            del item_to_sanitise[key]
        else:
            sanitised_key = sanitise(value)

            if sanitised_key is None:
                del item_to_sanitise[key]
            else:
                item_to_sanitise[key] = sanitised_key
    return item_to_sanitise


def _sanitise_list(item):
    item_to_sanitise = item.copy()
    sanitised_index = 0
    for list_item in item:
        sanitised_index = sanitised_index + 1
        if list_item is None:
            item_to_sanitise.remove(list_item)
            sanitised_index = sanitised_index - 1
        elif isinstance(list_item, (str, list, dict)):
            if len(list_item) == 0:
                item_to_sanitise.remove(list_item)
                sanitised_index = sanitised_index - 1
            elif isinstance(list_item, dict):
                sanitised_item = _sanitise_dictionary(list_item)
                if sanitised_item is None:
                    item_to_sanitise.remove(list_item)
                    sanitised_index = sanitised_index - 1
                else:
                    item_to_sanitise.remove(list_item)
                    item_to_sanitise.insert(sanitised_index, sanitised_item)
            elif isinstance(list_item, list):
                sanitised_item = _sanitise_list(list_item)
                if sanitised_item is None:
                    item_to_sanitise.remove(list_item)
                    sanitised_index = sanitised_index - 1
                else:
                    item_to_sanitise.remove(list_item)
                    item_to_sanitise.insert(sanitised_index, sanitised_item)

    return item_to_sanitise
