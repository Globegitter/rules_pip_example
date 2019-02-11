# rules_pip_example

This expects bazel >=0.23rc1 which can be downloaded here: https://releases.bazel.build/0.23.0/rc1/index.html

- To run the app: `bazel run //:app`
- To run tests: `bazel test //...`
- New requirements are added to the `requirements.in` followed by `bazel run //:pip-compile` to update the `requirements.txt`