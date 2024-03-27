import os
import sys
import click
import re

def is_subdir(parent_dir, child_dir):
    parent_dir = os.path.abspath(parent_dir)
    child_dir = os.path.abspath(child_dir)
    return os.path.commonprefix([parent_dir, child_dir]) == parent_dir
def create_directory_structure(tree_output, base_dir):
    current_path = '.'
    level_stack = []
    lines = tree_output.split('\n')[1:]  # Skip the first line which is the root
    for i, line in enumerate(lines):
        if line.strip():
            line_split = re.split(r"├──|└──", line)
            level = line.count('│') if len(line_split) > 1 else 0
            item = line_split[-1].strip()

            # Determine if the current item is a directory or file by looking ahead
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_line_split = re.split(r"├──|└──", next_line)
                next_line_level = next_line.count('│') if len(next_line_split) > 1 else 0
                is_directory = next_line_level > level
            else:
                is_directory = False  # Assume it's a file if it's the last line

            if not level_stack or level > level_stack[-1]:
                current_path = os.path.join(current_path, item)
                level_stack.append(level)
            elif level < level_stack[-1]:
                while level_stack and level < level_stack[-1]:
                    for _ in range(level_stack[-1] - level):
                        current_path = os.path.dirname(current_path)
                    level_stack.pop()
                current_path = os.path.join(os.path.dirname(current_path), item)
            else:
                current_path = os.path.join(os.path.dirname(current_path), item)

            # Panic if the path is not a subdirectory of the base directory
            if not is_subdir(base_dir, current_path):
                click.error(f"The directory '{current_path}' is outside the base directory '{base_dir}'.")

            # Create directory or file based on the peak ahead
            if is_directory:
                os.makedirs(os.path.join(base_dir, current_path), exist_ok=True)
            else:
                if not os.path.exists(os.path.join(base_dir, current_path)):
                    with open(os.path.join(base_dir, current_path), 'x'):
                        pass

@click.command()
@click.option('--base-dir', '-d', default='.', help='Base directory for the inverse tree structure.')
def inverse_tree(base_dir):
    """Recreate the directory structure from the output of the 'tree' command."""
    base_dir = os.path.abspath(base_dir)
    tree_output = sys.stdin.read()
    create_directory_structure(tree_output, base_dir)
    click.echo(f"Inverse tree structure created in '{base_dir}'.")

if __name__ == '__main__':
    inverse_tree()