# nd2file

A single-file pure Python `.nd2` (Nikon NIS-Elements) file reader.
This reader was developed initially as part of [molyso](https://github.com/modsim/molyso), in times where support for `.nd2` files was scarce.
It has been mainly used for multi position multi channel images, nothing besides that is implemented or tested (the `.nd2`-format supports various additional dimensions for multidimensional datasets).
The code is not really tidied up, but for our use cases it works (remarkably well).
Two things are different compared to most other `.nd2` readers I'm aware of: It uses memory-mapping, and has a heuristic fallback mode, in case damaged files (i.e. by crashed NIS instances) are opened, it can often *guess* where each frame would be, and speed up reading that way.
Undocumented, experimental, subject to change without notice, no guarantees it opens any files. Licensed BSD. 

## Example

```python
from nd2file import ND2MultiDim

nd2 = ND2MultiDim('test.nd2')

# informations about dimensionality
print(nd2.multipointcount)
print(nd2.timepointcount)

# calibration
print(nd2.calibration)

# image data
print(nd2.image_singlechannel(multipoint=5, timepoint=7, channel=0))
```
