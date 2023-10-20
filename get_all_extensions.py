import os


def get_all_extensions(dir):
    """
    Gets all the extensions and the count of all files in the current directory.
    """
    extensions = {}
    for filename in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, filename)):
            # gets the filename and extensions of each file
            fname, ext = os.path.splitext(filename)
            if ext not in extensions:
                extensions[ext] = extensions.get(ext, 1)
            else:
                extensions[ext] += 1
    return extensions