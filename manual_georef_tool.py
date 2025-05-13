import cv2
import numpy as np

print("🖱️ This script is a template for manual pixel-to-GPS calibration.")
print("Use OpenCV or another viewer to get pixel coordinates of known features (intersections, etc).")
print("Then match them to real GPS coords (lon, lat).")
print("These control points can be added to other scripts to georeference overlays or vector layers.
")

print("Example format for CONTROL_POINTS:")
print(