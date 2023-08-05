import pytest

from runrex.text import Sentences
from runrex.text.ssplit import default_ssplit


@pytest.mark.parametrize(('text', 'n_sent', 'exp_indices'), [
    ('A sentence.\n Another sentence\nis here.',
     3, [(0, 12), (12, 30), (30, 38)]),
])
def test_default_ssplit(text, n_sent, exp_indices):
    for i, ((sent, start, end), (exp_start, exp_end)) in enumerate(zip(
            default_ssplit(text), exp_indices
    )):
        assert start == exp_start
        assert end == exp_end
        assert i < n_sent


@pytest.mark.parametrize(('text', 'n_sent', 'exp_indices'), [
    ('A sentence.\n Another sentence\nis here.',
     3, [(0, 11), (13, 29), (30, 38)]),
    ('This or that.\n\n \nThese and those.\n',
     2, [(0, 13), (17, 33)]),
])
def test_default_sentence_segmentation(text, n_sent, exp_indices):
    sents = Sentences(text, None)
    assert len(sents) == n_sent
    for sent, (exp_start, exp_end) in zip(sents, exp_indices):
        assert sent.start == exp_start
        assert sent.end == exp_end
