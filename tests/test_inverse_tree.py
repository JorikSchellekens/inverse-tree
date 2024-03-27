import os
import shutil
from click.testing import CliRunner
from inverse_tree.inverse_tree import inverse_tree

def test_inverse_tree():
    runner = CliRunner()
    with runner.isolated_filesystem():
        print(os.getcwd())
        # Create a sample tree output
        tree_output = '''
  ├── pytest
  │   ├── __init__.py
  │   ├── __main__.py
  │   ├── __pycache__
  │   │   ├── __init__.cpython-312.pyc
  │   │   └── __main__.cpython-312.pyc
  │   └── py.typed
  └── pytest-8.1.1.dist-info
'''

        # Run the inverse_tree command
        result = runner.invoke(inverse_tree, [tree_output.strip()])
        assert result.exit_code == 0
        assert "Inverse tree structure created in '.'" in result.output

        # Check if the directory structure is recreated correctly
        assert os.path.exists('dir1')
        assert os.path.exists('dir1/subdir1')
        assert os.path.exists('dir1/subdir1/file1.txt')
        assert os.path.exists('dir1/subdir1/file2.txt')
        assert os.path.exists('dir1/subdir2')
        assert os.path.exists('dir2')
        assert os.path.exists('dir2/file3.txt')
        assert os.path.exists('file4.txt')