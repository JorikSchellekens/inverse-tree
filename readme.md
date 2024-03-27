# Inverse Tree

A Python-based CLI tool that recreates the directory structure from the output of the 'tree' command.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/inverse-tree.git
```

2. Install the package:
```
cd inverse-tree
pip install .
```


## Usage

1. Run the 'tree' command and capture its output:
```
tree /path/to/directory | inverse-tree
```

Optionally, specify the base directory for the inverse tree structure:
tree /path/to/directory | inverse-tree --base-dir /path/to/base/directory