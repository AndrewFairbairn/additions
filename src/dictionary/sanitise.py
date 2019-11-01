def sanitise(object):
    """
    Works through a given object and removes dictionary attributes which have None Type or empty string values
    :param object: Object to sanitise
    :return: Sanitised dictionary
    """
    # We must copy this object as we will iterate through it but may remove nodes from it
    object_to_sanitise = object.copy()
    for key, value in object.items():
        # If the key is a dictionary then pass the value back into this method again
        if isinstance(value, dict):
            object_to_sanitise[key] = sanitise(value)
        elif value is None or value == "":
            del object_to_sanitise[key]

    return object_to_sanitise
