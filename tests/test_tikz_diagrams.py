#!/usr/bin/env python3
"""
Unit tests for TikZ diagram patterns in the HDX-AI presentation.

These tests validate that our TikZ diagrams follow best practices
to prevent common issues like:
- Unequal circle sizes (missing inner sep=0pt or text width)
- Labels overlapping with boxes (y-coordinate too low)
- Z-order issues (important nodes drawn before connecting lines)
"""

import re
import unittest
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent


class TestCircleSizeConsistency(unittest.TestCase):
    """Test that circles in diagrams have consistent sizing."""

    def setUp(self):
        """Load the LaTeX source files."""
        self.part1_path = PROJECT_ROOT / "hdx-ai-part1.tex"
        self.part2_path = PROJECT_ROOT / "hdx-ai-part2.tex"

        self.part1_content = ""
        self.part2_content = ""

        if self.part1_path.exists():
            self.part1_content = self.part1_path.read_text()
        if self.part2_path.exists():
            self.part2_content = self.part2_path.read_text()

    def find_circle_nodes(self, content: str) -> list[dict]:
        """Extract circle node definitions from TikZ code."""
        # Pattern for nodes with circle shape or minimum size (circles)
        pattern = r'\\node\[([^\]]*circle[^\]]*|[^\]]*minimum size[^\]]*)\]'
        matches = re.finditer(pattern, content)

        nodes = []
        for match in matches:
            options = match.group(1)
            nodes.append({
                'options': options,
                'has_inner_sep_0': 'inner sep=0pt' in options or 'inner sep=0' in options,
                'has_text_width': 'text width' in options,
                'has_minimum_size': 'minimum size' in options,
            })
        return nodes

    def find_multi_circle_diagrams(self, content: str) -> list[str]:
        """Find TikZ diagrams that have multiple circles that should be equal size."""
        # Look for tikzpicture environments with multiple circle nodes
        tikz_pattern = r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}'
        diagrams = []
        for match in re.finditer(tikz_pattern, content, re.DOTALL):
            tikz_content = match.group(1)
            # Count circles
            circle_count = len(re.findall(r'\\node\[[^\]]*circle[^\]]*\]', tikz_content))
            if circle_count >= 3:  # CIA Triad, Tetrad, etc.
                diagrams.append(tikz_content)
        return diagrams

    def test_equal_size_circles_have_inner_sep_zero(self):
        """In multi-circle diagrams (triad, tetrad), circles should have inner sep=0pt."""
        for name, content in [("part1", self.part1_content), ("part2", self.part2_content)]:
            if not content:
                continue

            diagrams = self.find_multi_circle_diagrams(content)
            for diagram in diagrams:
                nodes = self.find_circle_nodes(diagram)
                circle_nodes = [n for n in nodes if 'circle' in n['options'] and n['has_minimum_size']]

                for node in circle_nodes:
                    self.assertTrue(
                        node['has_inner_sep_0'],
                        f"Circle in {name} multi-circle diagram should have inner sep=0pt: {node['options']}"
                    )

    def test_equal_size_circles_have_text_width_or_short_content(self):
        """In multi-circle diagrams, circles with long text should have text width."""
        for name, content in [("part1", self.part1_content), ("part2", self.part2_content)]:
            if not content:
                continue

            diagrams = self.find_multi_circle_diagrams(content)
            for diagram in diagrams:
                nodes = self.find_circle_nodes(diagram)
                circle_nodes = [n for n in nodes if 'circle' in n['options'] and n['has_minimum_size']]

                # Check that at least some circles have text width (the ones with long labels)
                circles_with_text_width = [n for n in circle_nodes if n['has_text_width']]
                # If there are circles without text width, they should be allowed only if
                # the diagram overall handles text constraint (at least one has it)
                if circle_nodes and not circles_with_text_width:
                    # Check if this is a diagram with potentially long text
                    if 'Confidentiality' in diagram or 'Availability' in diagram:
                        self.fail(
                            f"Multi-circle diagram in {name} with long labels should have "
                            "text width on circles to prevent size expansion"
                        )


class TestLabelPositioning(unittest.TestCase):
    """Test that labels don't overlap with boxes."""

    def setUp(self):
        """Load the LaTeX source files."""
        self.part2_path = PROJECT_ROOT / "hdx-ai-part2.tex"
        self.part2_content = ""

        if self.part2_path.exists():
            self.part2_content = self.part2_path.read_text()

    def extract_feedback_loops_diagram(self) -> str:
        """Extract the Feedback Loops TikZ diagram."""
        # Find the Feedback Loops frame
        pattern = r'\\begin\{frame\}\{Feedback Loops\}(.*?)\\end\{frame\}'
        match = re.search(pattern, self.part2_content, re.DOTALL)
        return match.group(1) if match else ""

    def test_inputs_outputs_labels_above_boxes(self):
        """Inputs and Outputs labels should have y > 1.0 to be above boxes."""
        diagram = self.extract_feedback_loops_diagram()
        if not diagram:
            self.skipTest("Feedback Loops diagram not found")

        # Find standalone label nodes (not attached to arrows)
        # Pattern: \node at (x, y) {Label};
        label_pattern = r'\\node at \((-?[\d.]+),\s*([\d.]+)\) \{(Inputs|Outputs)\}'
        matches = re.finditer(label_pattern, diagram)

        found_labels = False
        for match in matches:
            found_labels = True
            x, y, label = match.groups()
            y = float(y)
            self.assertGreaterEqual(
                y, 1.0,
                f"Label '{label}' y-coordinate ({y}) should be >= 1.0 to avoid box overlap"
            )

        if not found_labels:
            # Check if labels are inline with arrows (bad pattern)
            inline_pattern = r'\\draw.*node\[midway,\s*above\]\s*\{(Inputs|Outputs)\}'
            inline_matches = re.findall(inline_pattern, diagram)
            if inline_matches:
                self.fail(
                    f"Labels {inline_matches} use inline 'node[midway, above]' which causes overlap. "
                    "Use standalone \\node at (x, y) with y >= 1.0 instead."
                )


class TestZOrder(unittest.TestCase):
    """Test that z-order is correct in diagrams."""

    def setUp(self):
        """Load the LaTeX source files."""
        self.part2_path = PROJECT_ROOT / "hdx-ai-part2.tex"
        self.part2_content = ""

        if self.part2_path.exists():
            self.part2_content = self.part2_path.read_text()

    def extract_ot_tetrad_diagram(self) -> str:
        """Extract the OT Security Tetrad TikZ diagram."""
        # Match various title formats: "OT Security Tetrad" or "The OT Security Tetrad: Adding Safety"
        pattern = r'\\begin\{frame\}\{.*?OT Security Tetrad.*?\}(.*?)\\end\{frame\}'
        match = re.search(pattern, self.part2_content, re.DOTALL)
        return match.group(1) if match else ""

    def test_safety_node_drawn_after_lines(self):
        """Safety node should be drawn after connecting lines for correct z-order."""
        diagram = self.extract_ot_tetrad_diagram()
        if not diagram:
            self.skipTest("OT Tetrad diagram not found")

        # Find positions of Safety node definition and line draws
        safety_pattern = r'\\node.*\(safety\)'
        line_pattern = r'\\draw.*--.*safety|\\draw.*safety.*--'

        safety_match = re.search(safety_pattern, diagram)
        line_matches = list(re.finditer(line_pattern, diagram))

        if safety_match and line_matches:
            safety_pos = safety_match.start()
            # Safety should be drawn AFTER lines that connect to it
            for line_match in line_matches:
                if 'safety' in line_match.group():
                    self.assertGreater(
                        safety_pos, line_match.start(),
                        "Safety node should be drawn after connecting lines for correct z-order"
                    )


class TestDiagramCompilation(unittest.TestCase):
    """Test that diagrams compile without errors."""

    def setUp(self):
        """Check if xelatex is available."""
        import shutil
        self.xelatex = shutil.which('xelatex')
        if not self.xelatex:
            self.skipTest("xelatex not available")

    def test_part1_compiles(self):
        """Part 1 should compile without errors."""
        import subprocess
        result = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'hdx-ai-part1.tex'],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=120
        )
        self.assertEqual(result.returncode, 0, f"Part 1 compilation failed:\n{result.stdout[-2000:]}")

    def test_part2_compiles(self):
        """Part 2 should compile without errors."""
        import subprocess
        result = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'hdx-ai-part2.tex'],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=120
        )
        self.assertEqual(result.returncode, 0, f"Part 2 compilation failed:\n{result.stdout[-2000:]}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
