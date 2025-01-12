import pytest
import sys


class TestSkip:
    @pytest.mark.skip("Skipping this test case")
    def test_skip01(self):
        assert 1 == 1

    @pytest.mark.skipif(
        sys.version_info > (3, 7), reason="Skip if version is greater than 3.7"
    )
    def test_run01(self):
        assert 1 == 1

    @pytest.mark.skipif(sys.platform == "mac", reason="Skip if platform is windows")
    def test_run02(self):
        assert 1 == 1


    def run03(name):
        if name == "john":
            return "john"
        else:
            return "johny"

    @pytest.mark.skipif(run03("john") == "john", reason="Skip if name is john")
    def test_run04(self):
        assert 1 == 1
