import json
import os
import random
import string
import copy
import serverly


def ranstr(size=20, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    """return a random str with length `size` with the members of `chars`, e.g. only lowercase = 'abcde...'"""
    return ''.join(random.choice(chars) for x in range(size))


def check_relative_path(path: str):
    """Check if a path is valid as a web address. Returns True if valid, else raises different kinds of errors"""
    if type(path) == str:
        if path[0] == "/" or (path[0] == "^" and path[1] == "/"):
            return True
        else:
            raise ValueError(f"'{path}' (as a path) doesn't start with '/'.")
    else:
        raise TypeError("path not valid. Expected to be of type string.")


def get_http_method_type(method: str):
    """Return lowercase http method name, if valid. Else, raise Exception."""
    supported_methods = ["get", "post", "put", "delete"  # , "head", "connect", "options", "trace", "patch"
                         ]
    method = str(method.lower())
    if not method in supported_methods:
        raise Exception(
            "Request method not supported. Supported are GET, POST, PUT & DELETE.")
    return method


def check_relative_file_path(file_path: str):
    if type(file_path) == str:
        if os.path.isfile(file_path) or file_path.lower() == "none":
            return file_path
        else:
            raise FileNotFoundError(f"File '{file_path}' not found.")
    else:
        raise TypeError(
            "file_path argument expected to be of type string.")


def parse_response_info(info: dict, content_length=0):
    response_code = 200
    content_length = content_length
    content_type = "text/plain"
    overflow = {}
    for key, value in info.items():
        if key.lower() == "response_code" or key.lower() == "response code" or key.lower() == "code" or key.lower() == "response" or key.lower() == "responsecode":
            response_code = value
        elif key.lower() == "content-length" or key.lower() == "content_length" or key.lower() == "content length" or key.lower() == "length":
            content_length = value
        elif key.lower() == "content-type" or key.lower() == "content_type" or key.lower() == "content type" or key.lower() == "type":
            content_type = value
        else:
            overflow[key] = value
    info = {"Content-Length": content_length,
            "Content-type": content_type, **overflow}
    return response_code, info


def guess_filetype_on_filename(filename):
    file_types = {
        "html": "text/html"
    }
    ext = filename.split(".")[-1]
    return file_types.get(ext.lower(), "text/plain")


def guess_response_info(content: str):
    if content.startswith("<!DOCTYPE html>") or content.startswith("<html"):
        c_type = "text/html"
    else:
        try:
            if type(content) == str:
                json.loads(content)
            else:
                json.dumps(content)
            c_type = "application/json"
        except json.JSONDecodeError:
            c_type = "text/plain"
    return {"Content-type": c_type, "Content-Length": len(content)}


def clean_user_object(user_s):
    """return cleaned version (dict!!!) of object passed in. user_s can be of type User or list[User]."""
    bad_attributes = ["id", "password", "salt",
                      "bearer_token", "metadata", "to_dict"]

    def clean(u):
        new = {}
        for attr in dir(u):
            if not callable(attr) and not attr.startswith("_") and not attr in bad_attributes:
                new[attr] = getattr(u, attr)
        return new
    if type(user_s) == list:
        return [clean(u) for u in user_s]
    return clean(user_s)
