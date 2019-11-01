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

    return item_to_sanitise


def _sanitise_dictionary(dictionary):
    # We must copy this object as we will iterate through it but may remove nodes from it
    dict_to_sanitise = dictionary.copy()
    for key, value in dictionary.items():
        # If the key is a dictionary then pass the value back into this method again
        if isinstance(value, dict):
            if len(dict_to_sanitise[key]) == 0:
                del dict_to_sanitise[key]
            else:
                sanitised_key = sanitise(value)

                if sanitised_key is None:
                    del dict_to_sanitise[key]
                else:
                    dict_to_sanitise[key] = sanitised_key

        elif value is None or value == "":
            del dict_to_sanitise[key]
        else:
            sanitised_key = sanitise(value)

            if sanitised_key is None:
                del dict_to_sanitise[key]
            else:
                dict_to_sanitise[key] = sanitised_key
    return dict_to_sanitise
