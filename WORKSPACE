load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "com_apt_itude_rules_pip",
    commit = "ef384eef9d214e04a54dbfe6af018db89407bbaf",
    remote = "https://github.com/ecosia/rules_pip.git",
)

load("@com_apt_itude_rules_pip//rules:dependencies.bzl", "pip_rules_dependencies")

pip_rules_dependencies()

load("//:py.bzl", "PY3_PATH")
load("@com_apt_itude_rules_pip//rules:repository.bzl", "pip_repository")

pip_repository(
    name = "py3_deps",
    requirements = "//:requirements.txt",
    python_interpreter = PY3_PATH,
    wheel_cache = "~/.cache/bazel/wheels",
    quiet = True,
)