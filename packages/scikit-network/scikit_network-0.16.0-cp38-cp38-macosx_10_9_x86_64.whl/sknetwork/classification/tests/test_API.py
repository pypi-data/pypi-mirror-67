#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for classification API"""

import unittest

from sknetwork.classification import *
from sknetwork.data.test_graphs import *
from sknetwork.data import movie_actor
from sknetwork.embedding import GSVD


class TestClassificationAPI(unittest.TestCase):

    def test_undirected(self):
        adjacency = test_graph()
        adjacency_bool = test_graph_bool()
        n = adjacency.shape[0]
        seeds_array = -np.ones(n)
        seeds_array[:2] = np.arange(2)
        seeds_dict = {0: 0, 1: 1}

        classifiers = [PageRankClassifier(), DiffusionClassifier(), KNN(embedding_method=GSVD(3), n_neighbors=1),
                       CoPageRankClassifier(), Propagation()]
        for clf in classifiers:
            labels1 = clf.fit_transform(adjacency, seeds_array)
            labels2 = clf.fit_transform(adjacency, seeds_dict)
            labels3 = clf.fit_transform(adjacency_bool, seeds_array)
            self.assertTrue((labels1 == labels2).all())
            self.assertTrue((labels1 == labels3).all())
            self.assertEqual(labels2.shape[0], n)
            self.assertTupleEqual(clf.membership_.shape, (n, 2))

        seeds1 = {0: 0, 1: 1}
        seeds2 = {0: 0, 1: 2}
        for clf in classifiers:
            labels1 = (clf.fit_transform(adjacency, seeds1) == 1)
            labels2 = (clf.fit_transform(adjacency, seeds2) == 2)
            self.assertTrue((labels1 == labels2).all())

    def test_bipartite(self):
        biadjacency = movie_actor(metadata=False)
        n_row, n_col = biadjacency.shape
        seeds_row_array = -np.ones(n_row)
        seeds_row_array[:2] = np.arange(2)
        seeds_row_dict = {0: 0, 1: 1}
        seeds_col_dict = {0: 0}

        classifiers = [BiPageRankClassifier(), BiDiffusionClassifier(), BiKNN(embedding_method=GSVD(3), n_neighbors=1),
                       CoPageRankClassifier(), BiPropagation()]
        for clf in classifiers:
            clf.fit(biadjacency, seeds_row_array)
            labels_row1, labels_col1 = clf.labels_row_, clf.labels_col_
            clf.fit(biadjacency, seeds_row_dict)
            labels_row2, labels_col2 = clf.labels_row_, clf.labels_col_

            self.assertTrue(np.allclose(labels_row1, labels_row2))
            self.assertTrue(np.allclose(labels_col1, labels_col2))
            self.assertEqual(labels_col2.shape[0], n_col)
            self.assertTupleEqual(clf.membership_row_.shape, (n_row, 2))
            self.assertTupleEqual(clf.membership_col_.shape, (n_col, 2))

            clf.fit(biadjacency, seeds_row_dict, seeds_col_dict)
