import pytest
from mtpiclick.click import window
from mtpiclick.snagit.capture import capture

@pytest.fixture(scope="module")
def snagit():
    path = r"C:\Program Files\TechSmith\Snagit 2022\snagitcapture.exe"
    reference = capture.reference
    return window(path, reference)

def test_start(snagit):
    snagit.click(capture.start)
