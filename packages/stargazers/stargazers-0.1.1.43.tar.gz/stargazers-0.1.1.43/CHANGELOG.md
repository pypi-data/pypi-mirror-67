# stargazers
A collection of utilities to work with astronomical data

# 0.2 (WIP)
* Hacked together a multiscale optical flow approach. Made a pyramid scheme that
  works on various scales (configurable by parameter), finds the warping fields
  for every scale, and applies them.
  * Special case used in the `align.chromatic` function.
  * General case available in `flow` module: `multi_flow`, `multi_warp`, and
    `multi_tween`. Usage is the same as `get_flow`, `warp` and `tween`, but
    instead of one flow map, the `flows` argument is expected to be a list of
    optical flows, as returned by `multi_flow`.

# 0.1.1
Uploaded to PyPI.

# 0.1
* Added proper changelog, the one you're currently reading.
* Organized a lot of the modules. This version includes the following modules:
  * align, colors, denoise, edit, flow, gifs, gradients, io, transform, vfx,
    video.
  * Things **will move around** for a few minor versions, as there are some big
    modules missing (for example, morphological operations). Some functionality
    now resides in modules where it's comfortable to have it, but isn't really
    the best place for it.
* Version scheme is: major.minor.micro.nano.
  * Major is for big milestones. Someday will reach 1.0.
  * Minor is for a decently sized grouping of smaller changes. 0.1 groups about
    40 micro versions.
  * Micro is for a feature or sufficiently important fix.
  * Nano is sort of equivalent to a build number.