import os

import pytest

import invert


def test_createImage():
   # invert.process(["~/ccf/DockerTestAlgorithm/Data/testImage.jpg"])
    print(os.getcwd() + "Dir")
    assert os.path.isfile("fixed.jpeg")
   # os.remove("fixed.jpeg")
