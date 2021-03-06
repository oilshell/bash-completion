import pytest


class TestScreen:

    @pytest.mark.complete("screen -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.xfail  # TODO: whitespace split issue
    @pytest.mark.complete("screen -c shared/default/")
    def test_2(self, completion):
        assert completion.list == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("screen cat ")
    def test_3(self, completion):
        assert completion.list

    # Assume at least vt100 and friends are there
    @pytest.mark.complete("screen -T vt")
    def test_4(self, completion):
        assert completion.list

    @pytest.mark.complete("screen -T foo cat")
    def test_5(self, completion):
        assert completion.list
