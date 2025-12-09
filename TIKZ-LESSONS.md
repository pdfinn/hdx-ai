# TikZ Diagram Lessons Learned

Hard-won knowledge from building the CIA Triad and OT Tetrad diagrams.

## 1. `minimum size` Does NOT Guarantee Equal Sizes

**Problem**: Setting `minimum size=2cm` on all nodes resulted in different-sized circles.

**Root cause**: `minimum size` sets the *minimum* - nodes will **expand** to fit their text content. Longer words like "Confidentiality" make circles larger than "Integrity".

**Solution**: Use `inner sep=0pt` combined with `text width` to constrain text:
```latex
\node[circle, minimum size=2.4cm, inner sep=0pt, text width=2cm, align=center] {Confiden-\\tiality};
```

## 2. `scale` Does NOT Scale Node Sizes

**Problem**: Using `scale=0.5` on a tikzpicture still resulted in overlapping circles.

**Root cause**: The `scale` parameter only scales **coordinates**, not node dimensions like `minimum size`. So circles stay 2cm while positions are halved.

**Solution**: Don't use `scale` for sizing. Use absolute cm values for both positions and node sizes:
```latex
% WRONG - circles overlap despite larger coordinates
\begin{tikzpicture}[scale=0.5]
    \node[minimum size=2cm] at (0,4) {...};  % Position halved, size unchanged
\end{tikzpicture}

% CORRECT - use absolute values
\begin{tikzpicture}
    \node[minimum size=2.4cm] at (0,2.8) {...};
\end{tikzpicture}
```

## 3. Z-Order: Draw Order Matters

**Problem**: Lines appeared on top of a center node.

**Root cause**: TikZ draws elements in order - later elements appear on top.

**Solution**: Draw lines before the node that should appear on top:
```latex
% Define position as coordinate first
\coordinate (center) at (0,0);

% Draw outer nodes
\node (outer1) at (0,3) {...};

% Draw lines to the coordinate
\draw (outer1) -- (center);

% Draw center node LAST so it's on top
\node at (center) {...};
```

## 4. Orthogonal (Right-Angle) Paths

**Problem**: Needed right-angle connections instead of diagonal lines.

**Solution**: Use intermediate waypoints:
```latex
% Diagonal (default)
\draw (a) -- (b);

% Orthogonal - specify waypoints
\draw (a) -- (a |- b) -- (b);  % Go vertical first, then horizontal
% OR
\draw (a) -| (b);  % Shorthand: horizontal then vertical
\draw (a) |- (b);  % Shorthand: vertical then horizontal
```

## 5. Text in Circles

For text to fit in circles without expanding them:

1. Use `inner sep=0pt` - removes internal padding
2. Use `text width=Xcm` - constrains text width (should be < diameter)
3. Use `align=center` - centers multi-line text
4. Break long words manually with `\\`: `Confiden-\\tiality`
5. Use appropriate font size (`\tiny`, `\scriptsize`, `\small`)

## 6. Calculating Non-Overlapping Positions

For circles to not touch:
- Center-to-center distance must be > sum of radii
- For same-size circles: distance > diameter
- Add a small buffer for visual clarity

Example for 2.4cm diameter circles:
```latex
% Minimum distance = 2.4cm, use 2.8cm for breathing room
\node[minimum size=2.4cm] at (0,0) {Center};
\node[minimum size=2.4cm] at (0,2.8) {Top};      % 2.8cm away
\node[minimum size=2.4cm] at (-2.8,0) {Left};   % 2.8cm away
```

## Quick Reference

```latex
% Equal-sized circles with text that fits
\node[circle,
      fill=purple,
      text=white,
      minimum size=2.4cm,    % Desired size
      inner sep=0pt,         % Prevent text expansion
      text width=2cm,        % Constrain text width
      align=center,          % Center multi-line text
      font=\scriptsize\bfseries
] at (x,y) {Long\\Word};
```
