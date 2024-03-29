from app.models.relations import COMPOSER, READER, MUSICIAN
from django.db import connection
from django.http import Http404
from typing import List, Dict
import pathlib
from pydub import AudioSegment
import math


def return_or_404(f, message=None, **kwargs):
    try:
        return f(**kwargs)
    except IndexError:
        if message is not None:
            raise Http404(message)
        else:
            raise Http404


def normalize(arr):
    max_val = abs(max(arr, key=abs))
    return list(map(lambda x: round((x / max_val), 4), arr))


def get_peaks_from_audio_path(file) -> List[float]:
    """

    :param file: Could be a string or file object
    :return: a list of 1000 normalized samples from the audio file
    """

    audio = AudioSegment.from_file(file)
    audio = audio.set_channels(1)
    audio = audio.get_array_of_samples()
    # We want to get about a thousand samples for drawing the waveform
    every_nth = math.floor(len(audio) / 1000)
    sliced_samples = audio[0::every_nth]
    return normalize(sliced_samples)


def get_extension(path: str) -> str:
    """
    :param path: returns the extension of the file without the .
    :return: file extension e.g. jpg, wav
    """
    return pathlib.PurePosixPath(path).suffix.replace('.', '')


def to_none(s):
    """Converts identity objects to None"""
    if s is None:
        return s
    if type(s) is dict and not s:
        return None
    if type(s) is list and not s:
        return []
    if type(s) is str and not s.strip():
        return None
    return s


def to_dict(cursor):
    """
    Return all rows from a cursor as a dict
    :param cursor:
    :return:
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def sort_entities(entity_ls: List[Dict[str, str]]):
    composers = [i for i in entity_ls if i['relationship'] == COMPOSER]
    interpreters = [i for i in entity_ls if i['relationship'] in [READER, MUSICIAN]]
    others = [i for i in entity_ls if i['relationship'] not in [READER, MUSICIAN, COMPOSER]]
    return {
        'composers': composers,
        'interpreters': interpreters,
        'others': others
    }


def query(query_string: str, query_args: List) -> List[Dict]:
    with connection.cursor() as cursor:
        cursor.execute(query_string, query_args)
        return to_dict(cursor)


def get_dashed_location(model_dict):
    return get_dashed_list(['city', 'country'], model_dict)


def get_dashed_name(model_dict: Dict[str, str]) -> str:
    return get_dashed_list(['full_name', 'alt_name'], model_dict)


def get_dashed_date(model_dict: Dict[str, str]) -> str:
    return get_dashed_list(['start_date', 'end_date'], model_dict)


def get_dashed_list(key_ls, d) -> str:
    str_ls = [d[k] for k in key_ls]
    return ' - '.join([x for x in str_ls if x is not None])
