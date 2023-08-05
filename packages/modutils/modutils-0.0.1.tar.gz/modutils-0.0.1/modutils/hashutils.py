import re
import os

from hashlib import sha256

sha256_pattern: re.Pattern = re.compile('[A-Fa-f0-9]{64}')  # non case sensitive matching, can return non unique
hashutils_raise_exception: bool = False


def sha256_from_file(filepath: str) -> list:
    sha256_list: list = []
    if os.path.exists(filepath) and os.path.isfile(filepath):
        with open(filepath, 'r') as fin:
            sha256_list.extend(set(sha256_pattern.findall(fin.read())))
    else:
        if hashutils_raise_exception:
            raise FileNotFoundError(f'Filepath was not found {filepath!r}')
    return sha256_list


def sha256_from_dir(directory: str) -> list:
    sha256_list: list = []
    if os.path.exists(directory) and os.path.isfile(directory):
        files = [
            os.path.join(directory, path) for path in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, path))
        ]
        for filepath in files:
            sha256_list.extend(sha256_from_file(filepath))
    return sha256_list


def sha256_from_dir_map(directory: str) -> dict:
    sha256_map: dict = {}
    if os.path.exists(directory) and os.path.isfile(directory):
        files = [
            os.path.join(directory, path) for path in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, path))
        ]
        for filepath in files:
            sha256_map.update({filepath: sha256_from_file(filepath)})
    return sha256_map


def calc_sha256_from_dir(directory: str) -> list:
    sha256_list: list = []
    if os.path.exists(directory) and os.path.isfile(directory):
        files = [
            os.path.join(directory, path) for path in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, path))
        ]
        for filepath in files:
            with open(filepath, 'rb') as fin:
                sha256_list.append(sha256(fin.read()).hexdigest())
    return sha256_list

def calc_sha256_from_dir_map(directory: str) -> dict:
    sha256_map: dict = {}
    if os.path.exists(directory) and os.path.isfile(directory):
        files = [
            os.path.join(directory, path) for path in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, path))
        ]
        for filepath in files:
            with open(filepath, 'rb') as fin:
                sha256_map.update({filepath: sha256(fin.read()).hexdigest()})
    return sha256_map