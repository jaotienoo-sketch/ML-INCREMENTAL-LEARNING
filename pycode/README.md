# Python Code Guide
Create and activate a virtual environment with `venv` or `uv`, a fast Rust-based Python package and project manager.

## venv
python -m venv .knn-env
source .knn-env/bin/activate

## uv
uv venv .knn-env
source .knn-env/bin/activate

<h3 id="1-euclidean-distance" style="text-align:left"><span>1. Euclidean Distance</span></h3><p dir="ltr"><span>Euclidean distance is defined as the straight-line distance between two points in a plane or space. You can think of it like the shortest path you would walk if you were to go directly from one point to another.</span></p><blockquote><p dir="ltr"><gfg-tex>d( x, X_i ) = sqrt{sum_{j=1}^{n} ( x_j - X_{ij} )^2}</gfg-tex></p></blockquote>
