"""
Recursive Call Tree Tracer
Captures parent->child relationships, arguments, and return values for recursive functions.
Outputs SVG format.
"""

from functools import wraps
import itertools
from typing import Optional


class RecursiveTracer:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all tracking data"""
        self.call_id_gen = itertools.count()
        self.call_stack = []  # Stack of call IDs
        self.calls = {}  # call_id -> CallInfo
        self.edges = []  # (parent_id, child_id) tuples

    def trace(self, func):
        """Decorator to trace recursive function calls"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            call_id = next(self.call_id_gen)

            # Format arguments for display
            arg_strs = [self._format_arg(arg) for arg in args]
            kwarg_strs = ["{0}={1}".format(k, self._format_arg(v)) for k, v in kwargs.items()]
            all_args = ", ".join(arg_strs + kwarg_strs)

            # Record this call
            parent_id = self.call_stack[-1] if self.call_stack else None
            call_info = CallInfo(id=call_id, func_name=func.__name__, args_str=all_args, parent_id=parent_id)
            self.calls[call_id] = call_info

            # Record parent-child relationship
            if parent_id is not None:
                self.edges.append((parent_id, call_id))

            # Push onto call stack
            self.call_stack.append(call_id)

            try:
                # Execute the function
                result = func(*args, **kwargs)
                call_info.return_value = self._format_arg(result)
                return result
            finally:
                # Always pop from stack
                self.call_stack.pop()

        return wrapper

    def _format_arg(self, arg, max_len=40):
        """Format argument for display, truncating if too long"""
        arg_str = repr(arg)
        if len(arg_str) > max_len:
            return arg_str[: max_len - 3] + "..."
        return arg_str

    def generate_svg(self, filename="recursion_tree"):
        """Generate SVG file directly without creating DOT file"""
        if not self.calls:
            print("No function calls to visualize")
            return

        dot_content = self._generate_dot()

        # Try to render SVG directly using subprocess pipe
        try:
            import subprocess
            import os

            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            svg_filename = os.path.join(script_dir, "{0}.svg".format(filename))
            process = subprocess.Popen(
                ["dot", "-Tsvg"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            svg_output, error = process.communicate(input=dot_content)

            if process.returncode == 0:
                with open(svg_filename, "w") as f:
                    f.write(svg_output)
                print("Generated {0} (open in VS Code to view)".format(svg_filename))
            else:
                print("Error generating SVG: {0}".format(error))

        except (ImportError, FileNotFoundError):
            print("Graphviz not available for rendering. Install with: sudo apt install graphviz")

    def _generate_dot(self):
        """Generate DOT format string"""
        lines = [
            "digraph RecursionTree {",
            "    rankdir=TB;",
            "    node [shape=box, style=rounded, fontname=monospace];",
            "    edge [fontname=monospace];",
            "",
        ]

        # Add nodes
        for call_id, call_info in self.calls.items():
            call_sig = "{0}({1})".format(call_info.func_name, call_info.args_str)
            if call_info.return_value:
                label = "{0} -> {1}".format(call_sig, call_info.return_value)
            else:
                label = call_sig

            # Escape quotes and backslashes for DOT format
            label = label.replace('"', '\\"').replace("\\", "\\\\")
            lines.append('    {0} [label="{1}"];'.format(call_id, label))

        lines.append("")

        # Add edges
        for parent_id, child_id in self.edges:
            lines.append("    {0} -> {1};".format(parent_id, child_id))

        lines.append("}")
        return "\n".join(lines)


class CallInfo:
    """Information about a single function call"""

    def __init__(self, id, func_name, args_str, parent_id):
        self.id = id
        self.func_name = func_name
        self.args_str = args_str
        self.parent_id = parent_id
        self.return_value: Optional[str] = None  # or Union[str, None]


# Global tracer instance for convenience
tracer = RecursiveTracer()
trace_calls = tracer.trace
