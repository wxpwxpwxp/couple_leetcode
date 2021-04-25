# from pylint import epylint as lint
# (pylint_stdout, pylint_stderr) = lint.py_run('./problems/1-two_nums/siri.py --disable C0114', return_std=True)

# print(pylint_stdout, pylint_stderr)

import pylint.lint
pylint_opts = ['-h']
pylint.lint.Run(pylint_opts)
