import pytest


class TestFile:

    @pytest.mark.complete("file ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("file -")
    def test_2(self, completion):
        assert completion.list
