import pytest
import os
from PIL import Image
import vec2img.command

@pytest.fixture
def fixture_path():
    return os.path.join('tests', 'fixtures')

def test_convert(tmpdir, fixture_path):
    vec2img.command.convert(os.path.join(fixture_path, 'logo.vec'), 24, 24, str(tmpdir))
    assert len(tmpdir.listdir()) == 10
    
    for localpath in tmpdir.listdir():
        path1 = str(localpath)
        path2 = os.path.join(fixture_path, 'logo', os.path.basename(path1))
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        assert img1.size == img2.size
        assert list(img1.getdata()) == list(img2.getdata())
