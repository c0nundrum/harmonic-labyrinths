"""Generate the site's identity artwork (DESIGN.md §15). Run from the repository root:

    python3 tools/identity.py

Writes:
  static/images/triplet.svg          home figure: the trip-let and its two shadows
  layouts/_partials/mark.svg         header mark: the trip-let alone
  static/favicon.svg                 same as the mark
  layouts/_partials/figure-ground.svg footer: H and L as absence in a field of squares

The trip-let is a block of cubes whose projection along one axis is the letter
H and along the other is L, after the blocks on the cover of Hofstadter's
"Gödel, Escher, Bach". All artwork here is original; nothing is traced.
Standard library only.
"""
import math

H = ["X.X", "X.X", "XXX", "X.X", "X.X"]          # rows top→bottom, cols x
L = ["..X", "..X", "..X", "..X", "XXX"]          # rows top→bottom, cols z (stem at z=2 reads correctly)
ROWS, W = 5, 3
cell = lambda grid, row, col: grid[row][col] == "X"
# y=0 is the bottom row
vox = {(x, y, z) for x in range(W) for y in range(ROWS) for z in range(W)
       if cell(H, ROWS - 1 - y, x) and cell(L, ROWS - 1 - y, z)}

C, S = math.cos(math.radians(30)), math.sin(math.radians(30))
def iso(x, y, z, u):
    return ((x - z) * C * u, (-y + (x + z) * S) * u)

def poly(points, fill, u, stroke=None, sw=0):
    pts = " ".join(f"{px:.2f},{py:.2f}" for px, py in (iso(*p, u) for p in points))
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else f' stroke="{fill}" stroke-width="0.4" stroke-linejoin="round"'
    return f'<polygon points="{pts}" fill="{fill}"{st}/>'

def faces(x, y, z):
    out = []
    if (x, y + 1, z) not in vox:  # top
        out.append(("top", [(x, y+1, z), (x+1, y+1, z), (x+1, y+1, z+1), (x, y+1, z+1)]))
    if (x + 1, y, z) not in vox:  # +x face
        out.append(("px", [(x+1, y, z), (x+1, y+1, z), (x+1, y+1, z+1), (x+1, y, z+1)]))
    if (x, y, z + 1) not in vox:  # +z face
        out.append(("pz", [(x, y, z+1), (x+1, y, z+1), (x+1, y+1, z+1), (x, y+1, z+1)]))
    return out

def render(u, with_walls, colors, pad):
    els = []
    g = 2.0  # distance from block to walls
    if with_walls:
        top = ROWS + 1.0
        far = W + 1.0
        # wall behind along z (shows H), wall behind along x (shows L), floor
        els.append(poly([(-g, 0, -g), (far, 0, -g), (far, top, -g), (-g, top, -g)], colors["wall"], u, colors["edge"], 1))
        els.append(poly([(-g, 0, -g), (-g, 0, far), (-g, top, far), (-g, top, -g)], colors["wall"], u, colors["edge"], 1))
        els.append(poly([(-g, 0, -g), (far, 0, -g), (far, 0, far), (-g, 0, far)], colors["floor"], u, colors["edge"], 1))
        for x, y, z in vox:
            els.append(poly([(x, y, -g), (x+1, y, -g), (x+1, y+1, -g), (x, y+1, -g)], colors["shadow"], u))
            els.append(poly([(-g, y, z), (-g, y, z+1), (-g, y+1, z+1), (-g, y+1, z)], colors["shadow"], u))
    lift = 0.6 if with_walls else 0
    for x, y, z in sorted(vox, key=lambda v: (v[0] + v[1] + v[2], v[1])):
        for kind, pts in faces(x, y, z):
            els.append(poly([(px, py + lift, pz) for px, py, pz in pts], colors[kind], u))
    # bounds
    xs, ys = [], []
    for e in els:
        for pair in e.split('points="')[1].split('"')[0].split():
            a, b = map(float, pair.split(",")); xs.append(a); ys.append(b)
    minx, miny, maxx, maxy = min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad
    w, h = maxx - minx, maxy - miny
    return w, h, f'{minx:.2f} {miny:.2f} {w:.2f} {h:.2f}', "\n  ".join(els)

PALETTE = {"top": "#ffffff", "px": "#c6c6c6", "pz": "#8d8d8d", "wall": "#f4f4f4", "floor": "#ffffff",
           "shadow": "#161616", "edge": "#e0e0e0"}


def figure_svg():
    w, h, vb, body = render(16, True, PALETTE, 2)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w:.0f}" height="{h:.0f}" role="img" aria-labelledby="triplet-title">\n'
            f'  <title id="triplet-title">A block shaped so that light from one side casts an H on the wall behind it, and light from the other side casts an L.</title>\n  {body}\n</svg>\n')


def mark_svg():
    mark = dict(PALETTE, top="#ffffff", px="#8d8d8d", pz="#161616")
    w, h, vb, body = render(4, False, mark, 0.5)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w:.0f}" height="{h:.0f}" aria-hidden="true" focusable="false">\n'
            f'  {body}\n</svg>\n')


def figure_ground_svg():
    """A field of squares in which H and L exist only as absence."""
    rows, cols = 7, 11  # one-cell margin; H at columns 2-4, L at columns 6-8
    holes = set()
    for r in range(ROWS):
        for c in range(W):
            if H[r][c] == "X":
                holes.add((r + 1, c + 2))
            if L[r][W - 1 - c] == "X":  # L is stored mirrored for the trip-let
                holes.add((r + 1, c + 6))
    size, gap = 6, 2
    step = size + gap
    rects = [f'<rect x="{c * step}" y="{r * step}" width="{size}" height="{size}"/>'
             for r in range(rows) for c in range(cols) if (r, c) not in holes]
    w, h = cols * step - gap, rows * step - gap
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" focusable="false">\n'
            '  <g fill="currentColor">\n    ' + "\n    ".join(rects) + '\n  </g>\n</svg>\n')


if __name__ == "__main__":
    outputs = {
        "static/images/triplet.svg": figure_svg(),
        "layouts/_partials/mark.svg": mark_svg(),
        "static/favicon.svg": mark_svg(),
        "layouts/_partials/figure-ground.svg": figure_ground_svg(),
    }
    for path, svg in outputs.items():
        with open(path, "w") as f:
            f.write(svg)
        print("wrote", path)
