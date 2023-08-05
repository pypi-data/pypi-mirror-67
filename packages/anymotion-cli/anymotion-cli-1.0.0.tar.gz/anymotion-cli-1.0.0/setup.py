# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anymotion_cli', 'anymotion_cli.commands']

package_data = \
{'': ['*']}

install_requires = \
['anymotion-sdk>=1.0,<1.1',
 'click>=7.1.1,<8.0.0',
 'click_help_colors>=0.6,<0.7',
 'click_repl>=0.1.6,<0.2.0',
 'pygments>=2.6.1,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'tabulate>=0.8.6,<0.9.0',
 'yaspin>=0.16.0,<0.17.0']

entry_points = \
{'console_scripts': ['amcli = anymotion_cli.core:cli']}

setup_kwargs = {
    'name': 'anymotion-cli',
    'version': '1.0.0',
    'description': 'Command Line Interface for AnyMotion API',
    'long_description': '# AnyMotion CLI\n\n[![CircleCI][ci-status]][ci] [![codecov][codecov-status]][codecov]\n\nThis package provides a command line interface to [AnyMotion](https://anymotion.nttpc.co.jp/).\n\nIt works on Python versions:\n\n- Python 3.6\n- Python 3.7\n- Python 3.8\n\n## Installation\n\nInstall using [pip](https://pip.pypa.io/en/stable/quickstart/):\n\n```sh\n$ pip install anymotion-cli\n```\n\n## Getting Started\n\nBefore using anymotion-cli, you need to tell it about your credentials which issued by the [AnyMotion Portal](https://portal.anymotion.jp/).\nYou can do this in several ways:\n\n- CLI command\n- Credentials file\n- Environment variables\n\nThe quickest way to get started is to run the `amcli configure` command:\n\n```sh\n$ amcli configure\nAnyMotion API URL [https://api.customer.jp/anymotion/v1/]:\nAnyMotion Client ID: your_client_id\nAnyMotion Client Secret: your_client_secret\n```\n\nTo use environment variables, do the following:\n\n```sh\nexport ANYMOTION_CLIENT_ID=<your_client_id>\nexport ANYMOTION_CLIENT_SECRET=<your_client_secret>\n```\n\nTo use the credentials file, create an INI formatted file like this:\n\n```text\n[default]\nanymotion_client_id=<your_client_id>\nanymotion_client_secret=<your_client_secret>\n```\n\nand place it in `~/.anymotion/credentials`.\n\n**Note**: If set in both the credentials file and environment variables, the environment variables takes precedence.\n\n## Usage\n\nYou can use `amcli`.\n\n```text\namcli [OPTIONS] COMMAND [ARGS]...\n```\n\nMore information, see below tables or run with `--help` option.\n\n### Commands to process something (verb commands)\n\n| command name | description |\n| -- | -- |\n| upload | Upload the local movie or image file to the cloud storage. |\n| download | Download the drawn file. |\n| extract | Extract keypoints from uploaded images or movies. |\n| draw | Draw points and/or lines on uploaded movie or image. |\n| analyze | Analyze the extracted keypoint data. |\n\n### Commands to show something (noun commands)\n\n| command name | description |\n| -- | -- |\n| image | Show the information of the uploaded images. |\n| movie | Show the information of the uploaded movies. |\n| keypoint | Show the extracted keypoints. |\n| drawing | Show the information of the drawn images or movies. |\n| analysis | Show the analysis results. |\n\n### Other commands\n\n| command name | description |\n| -- | -- |\n| configure | Configure your AnyMotion Credentials. |\n\n### Examples\n\n#### Draw keypoints in image file\n\nFirst, upload the image file.\n\n```sh\n$ amcli upload image.jpg\nSuccess: Uploaded image.jpg to the cloud storage. (image id: 111)\n```\n\nWhen the upload is complete, you get an `image id`.\nExtract keypoints using this `image id`.\n\n```sh\n$ amcli extract --image-id 111\nKeypoint extraction started. (keypoint id: 222)\nSuccess: Keypoint extraction is complete.\n```\n\nDraw points/lines to image using `keypoint id`.\n\n```sh\n$ amcli draw 222\nDrawing is started. (drawing id: 333)\nSuccess: Drawing is complete.\nDownloaded the file to image.jpg.\n```\n\nWhen the drawing is complete, the drawing file is downloaded (by default, to the current directory).\nTo save to a specific file or directory, use the `--out` option.\n\n## Shell Complete\n\nThe anymotion-cli supports Shell completion.\n\nFor Bash, add this to `~/.bashrc`:\n\n```sh\neval "$(_AMCLI_COMPLETE=source amcli)"\n```\n\nFor Zsh, add this to `~/.zshrc`:\n\n```sh\neval "$(_AMCLI_COMPLETE=source_zsh amcli)"\n```\n\nFor Fish, add this to `~/.config/fish/completions/amcli.fish`:\n\n```sh\neval (env _AMCLI_COMPLETE=source_fish amcli)\n```\n\n## Change Log\n\nSee [CHANGELOG.md](CHANGELOG.md).\n\n## Contributing\n\n- Code must work on Python 3.6 and higher.\n- Code should follow [black](https://black.readthedocs.io/en/stable/).\n- Docstring should follow [Google Style](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).\n- Install all development dependencies using:\n\n  ```sh\n  $ poetry install\n  ```\n\n- Before submitting pull requests, run tests with:\n\n  ```sh\n  $ poetry run tox\n  ```\n\n[ci]: https://circleci.com/gh/nttpc/anymotion-cli\n[ci-status]: https://circleci.com/gh/nttpc/anymotion-cli.svg?style=shield&circle-token=4f7564ae447f53ff1c6d3aadb2303b5d526c6fb8\n[codecov]: https://codecov.io/gh/nttpc/anymotion-cli\n[codecov-status]: https://codecov.io/gh/nttpc/anymotion-cli/branch/master/graph/badge.svg?token=6S0GIV4ZD9\n',
    'author': 'Yusuke Kumihashi',
    'author_email': 'y_kumiha@nttpc.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nttpc/anymotion-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
