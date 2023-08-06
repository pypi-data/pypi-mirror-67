#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 15, 2019
@author: Quentin Lutz <qlutz@enst.fr>
"""

import pickle
import tarfile
import shutil
from os import environ, makedirs, remove, listdir, rmdir
from os.path import exists, expanduser, join, isabs
from typing import Optional, Union
from urllib.error import HTTPError
from urllib.request import urlretrieve

import numpy as np
from scipy import sparse

from sknetwork.data.parse import parse_tsv, parse_labels, parse_header, parse_metadata
from sknetwork.utils import Bunch
from sknetwork.utils.check import is_square


def get_data_home(data_home: Optional[str] = None):
    """
    Return a path to a storage folder depending on the dedicated environment variable and user input.

    Parameters
    ----------
    data_home: str
        The folder to be used for dataset storage
    """
    if data_home is None:
        data_home = environ.get('SCIKIT_NETWORK_DATA',
                                join('~', 'scikit_network_data'))
    data_home = expanduser(data_home)
    if not exists(data_home):
        makedirs(data_home)
    return data_home


def clear_data_home(data_home: Optional[str] = None):
    """
    Clear storage folder depending on the dedicated environment variable and user input.

    Parameters
    ----------
    data_home: str
        The folder to be used for dataset storage
    """
    data_home = get_data_home(data_home)
    shutil.rmtree(data_home)


def load_netset(dataset: Optional[str] = None, data_home: Optional[str] = None) -> Bunch:
    """Load a dataset from the `NetSets database
    <https://graphs.telecom-paristech.fr/>`_.

    Parameters
    ----------
    dataset : str
        The name of the dataset (all low-case). Examples include 'openflights', 'cinema' and 'wikivitals'.
    data_home : str
        The folder to be used for dataset storage.

    Returns
    -------
    graph : :class:`Bunch`

    Example
    -------
    >>> from sknetwork.data import load_netset
    >>> graph = load_netset('openflights')
    >>> graph.adjacency.shape
    (3097, 3097)
    """
    graph = Bunch()

    if dataset is None:
        print("Please specify the dataset (e.g., 'openflights' or 'wikivitals').\n" +
              "Complete list available here: <https://graphs.telecom-paristech.fr/datasets_npz/>")
        return graph
    if data_home is None:
        data_home = get_data_home()
    data_path = data_home + '/' + dataset + '/'
    if not exists(data_path):
        makedirs(data_path, exist_ok=True)
        try:
            urlretrieve("https://graphs.telecom-paristech.fr/datasets_npz/" + dataset + '_npz.tar.gz',
                        data_home + '/' + dataset + '_npz.tar.gz')
        except HTTPError:
            rmdir(data_home + '/' + dataset)
            raise ValueError('Invalid dataset: ' + dataset + '.'
                             + "\nAvailable datasets include 'openflights' and 'wikivitals'."
                             + "\nSee <https://graphs.telecom-paristech.fr/>")
        with tarfile.open(data_home + '/' + dataset + '_npz.tar.gz', 'r:gz') as tar_ref:
            tar_ref.extractall(data_home)
        remove(data_home + '/' + dataset + '_npz.tar.gz')

    files = [file for file in listdir(data_path)]

    for file in files:
        file_components = file.split('.')
        if len(file_components) == 2:
            file_name, file_extension = tuple(file_components)
            if file_extension == 'npz':
                graph[file_name] = sparse.load_npz(data_path + '/' + file)
            elif file_extension == 'npy':
                graph[file_name] = np.load(data_path + '/' + file)
            elif file_extension == 'p':
                graph[file_name] = pickle.load(open(data_path + '/' + file, 'rb'))

    return graph


def load_konect(dataset: str, data_home: Optional[str] = None, auto_numpy_bundle: bool = True) -> Bunch:
    """Load a dataset from the `Konect database
    <http://konect.uni-koblenz.de>`_.

    Parameters
    ----------
    dataset : str
        The name of the dataset as specified in the download link (e.g. for the Actor movies dataset, the corresponding
        name is ``'actor-movie'``).
    data_home : str
        The folder to be used for dataset storage
    auto_numpy_bundle : bool
        Denotes if the dataset should be stored in its default format (False) or using Numpy files for faster
        subsequent access to the dataset (True).

    Returns
    -------
    graph : :class:`Bunch`
        An object with the following attributes:

             * `adjacency` or `biadjacency`: the adjacency/biadjacency matrix for the dataset
             * `meta`: a dictionary containing the metadata as specified by Konect
             * each attribute specified by Konect (ent.* file)

    Example
    -------
    >>> from sknetwork.data import load_konect
    >>> graph = load_konect('dolphins')
    >>> graph.adjacency.shape
    (62, 62)

    Notes
    -----
    An attribute `meta` of the `Bunch` class is used to store information about the dataset if present. In any case,
    `meta` has the attribute `name` which, if not given, is equal to the name of the dataset as passed to this function.
    """
    if dataset == '':
        raise ValueError("Please specify the dataset. "
                         + "\nExamples include 'actor-movie' and 'ego-facebook'."
                         + "\n See 'http://konect.uni-koblenz.de' for the full list.")
    if data_home is None:
        data_home = get_data_home()
    data_path = data_home + '/' + dataset + '/'
    if not exists(data_path):
        makedirs(data_path, exist_ok=True)
        try:
            urlretrieve('http://konect.uni-koblenz.de/downloads/tsv/' + dataset + '.tar.bz2',
                        data_home + '/' + dataset + '.tar.bz2')
            with tarfile.open(data_home + '/' + dataset + '.tar.bz2', 'r:bz2') as tar_ref:
                tar_ref.extractall(data_home)
        except (HTTPError, tarfile.ReadError):
            rmdir(data_home + '/' + dataset)
            raise ValueError('Invalid dataset ' + dataset + '.'
                             + "\nExamples include 'actor-movie' and 'ego-facebook'."
                             + "\n See 'http://konect.uni-koblenz.de' for the full list.")
        finally:
            remove(data_home + '/' + dataset + '.tar.bz2')
    elif exists(data_path + '/' + dataset + '_bundle'):
        return load_from_numpy_bundle(dataset + '_bundle', data_path)

    data = Bunch()

    files = [file for file in listdir(data_path) if dataset in file]

    matrix = [file for file in files if 'out.' in file]
    if matrix:
        file = matrix[0]
        directed, bipartite, weighted = parse_header(data_path + file)
        if bipartite:
            graph = parse_tsv(data_path + file, directed=directed, bipartite=bipartite, weighted=weighted)
            data.biadjacency = graph.biadjacency
        else:
            graph = parse_tsv(data_path + file, directed=directed, bipartite=bipartite, weighted=weighted)
            data.adjacency = graph.adjacency

    metadata = [file for file in files if 'meta.' in file]
    if metadata:
        file = metadata[0]
        data.meta = parse_metadata(data_path + file)

    attributes = [file for file in files if 'ent.' + dataset in file]
    if attributes:
        for file in attributes:
            attribute_name = file.split('.')[-1]
            data[attribute_name] = parse_labels(data_path + file)

    if hasattr(data, 'meta'):
        if hasattr(data.meta, 'name'):
            pass
        else:
            data.meta.name = dataset
    else:
        data.meta = Bunch()
        data.meta.name = dataset

    if auto_numpy_bundle:
        save_to_numpy_bundle(data, dataset + '_bundle', data_path)

    return data


def save_to_numpy_bundle(data: Bunch, bundle_name: str, data_home: Optional[str] = None):
    """Save a Bunch in the specified data home to a collection of Numpy and Pickle files for faster subsequent loads.

    Parameters
    ----------
    data: Bunch
        The data to save
    bundle_name: str
        The name to be used for the bundle folder
    data_home: str
        The folder to be used for dataset storage
    """
    data_path = data_home + bundle_name
    makedirs(data_path, exist_ok=True)
    for attribute in data:
        if type(data[attribute]) == sparse.csr_matrix:
            sparse.save_npz(data_path + '/' + attribute, data[attribute])
        elif type(data[attribute]) == np.ndarray:
            np.save(data_path + '/' + attribute, data[attribute])
        elif type(data[attribute]) == Bunch or type(data[attribute]) == str:
            pickle.dump(data[attribute], open(data_path + '/' + attribute + '.p', 'wb'))
        else:
            raise TypeError('Unsupported data attribute type '+str(type(data[attribute])) + '.')


def load_from_numpy_bundle(bundle_name: str, data_home: Optional[str] = None):
    """Load a Bunch from a collection of Numpy and Pickle files (inverse function of ``save_to_numpy_bundle``).

    Parameters
    ----------
    bundle_name: str
        The name used for the bundle folder
    data_home: str
        The folder used for dataset storage

    Returns
    -------
    data: Bunch
        The original data
    """
    data_path = data_home + bundle_name
    if not exists(data_path):
        raise FileNotFoundError('No bundle at ' + data_path)
    else:
        files = listdir(data_path)
        data = Bunch()
        for file in files:
            file_name, file_extension = file.split('.')
            if file_extension == 'npz':
                data[file_name] = sparse.load_npz(data_path + '/' + file)
            elif file_extension == 'npy':
                data[file_name] = np.load(data_path + '/' + file)
            elif file_extension == 'p':
                data[file_name] = pickle.load(open(data_path + '/' + file, 'rb'))
        return data


def save(folder: str, data: Union[sparse.csr_matrix, Bunch]):
    """Save a Bunch or a CSR matrix in the current directory to a collection of Numpy and Pickle files for faster
    subsequent loads.

    Parameters
    ----------
    folder : str
        The name to be used for the bundle folder
    data : Union[sparse.csr_matrix, Bunch]
        The data to save

    Example
    -------
    >>> from sknetwork.data import save
    >>> graph = Bunch()
    >>> graph.adjacency = sparse.csr_matrix(np.random.random((10, 10)) < 0.2)
    >>> graph.names = np.array(list('abcdefghij'))
    >>> save('random_data', graph)
    >>> 'random_data' in listdir('.')
    True
    """
    folder = expanduser(folder)
    if exists(folder):
        shutil.rmtree(folder)
    if isinstance(data, sparse.csr_matrix):
        bunch = Bunch()
        if is_square(data):
            bunch.adjacency = data
        else:
            bunch.biadjacency = data
        data = bunch
    if isabs(folder):
        save_to_numpy_bundle(data, folder, '')
    else:
        save_to_numpy_bundle(data, folder, './')


def load(folder: str):
    """Load a Bunch from a previously created bundle from the current directory (inverse function of ``save``).

    Parameters
    ----------
    folder: str
        The name used for the bundle folder

    Returns
    -------
    data: Bunch
        The original data

    Example
    -------
    >>> from sknetwork.data import save
    >>> graph = Bunch()
    >>> graph.adjacency = sparse.csr_matrix(np.random.random((10, 10)) < 0.2)
    >>> graph.names = np.array(list('abcdefghij'))
    >>> save('random_data', graph)
    >>> loaded_graph = load('random_data')
    >>> loaded_graph.names[0]
    'a'
    """
    if isabs(folder):
        return load_from_numpy_bundle(folder, '')
    else:
        return load_from_numpy_bundle(folder, './')
