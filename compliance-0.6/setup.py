# Copyright 2018 MLBenchmark Group. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import setuptools

with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
    name="mlperf_compliance",
    version="0.6.0",
    author="Taylor Robie",
    author_email="taylorrobie@google.com",
    description="Tools for logging MLPerf compliance tags.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlperf/training/tree/master/compliance",
    packages=['mlperf_compliance'],
    classifiers=[
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: Apache Software License",
      "Operating System :: OS Independent",
    ],
    license='Apache 2.0',
)
