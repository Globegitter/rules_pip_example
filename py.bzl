load("@com_apt_itude_rules_pip//tools/pytest:rules.bzl", "pytest_test")

PY3_PATH = "/usr/bin/python3.7"
PY2_PATH = "/usr/bin/python2.7"

def pytest3_test(name, src, **kwargs):
    pytest_test(
        name = name,
        src = src,
        python_version = "PY3",
        pytest_dep = "@py3_deps//pytest",
        interpreter_path = PY3_PATH,
        **kwargs
    )