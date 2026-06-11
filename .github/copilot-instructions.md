# Copilot Instructions

## Project Overview

This project is a real-time color detection application built using Python, OpenCV, and NumPy.

The application:

* Captures video frames from the webcam.
* Converts frames from BGR to HSV color space.
* Detects predefined colors using HSV boundaries.
* Displays the detected color on the video feed.
* Runs continuously until the user presses the ESC key.

---

## Technology Stack

* Python 3.x
* OpenCV (cv2)
* NumPy

---

## Project Structure

* `main.py` - Entry point of the application.
* `detector()` - Responsible for color detection using HSV color thresholds.
* `color_boundary` - Dictionary containing HSV ranges for supported colors.
* Webcam feed is processed frame-by-frame in a continuous loop.

---

## Supported Colors

The system currently supports:

* Red
* Green
* Blue
* Yellow
* Black
* White
* Gray
* Purple

When adding new colors:

* Use HSV ranges.
* Follow the existing dictionary structure.
* Keep color names lowercase.

---

## Coding Guidelines

### General

* Use descriptive variable names.
* Keep functions focused on a single responsibility.
* Add comments only when logic is not obvious.
* Prefer readability over micro-optimizations.

### OpenCV

* Use HSV color space for color detection.
* Avoid hardcoding duplicate HSV values.
* Reuse the `color_boundary` configuration when possible.
* Validate masks using `cv2.countNonZero()`.

### Error Handling

* Verify camera availability before processing frames.
* Handle failed frame captures gracefully.
* Avoid application crashes caused by camera disconnects.

### Performance

* Process frames in real time.
* Avoid unnecessary image copies.
* Keep per-frame computations lightweight.

---

## Preferred Code Style

* Follow PEP 8 conventions.
* Use snake_case for variables and functions.
* Keep line lengths reasonable.
* Use constants for configurable values.

---

## Future Enhancements

When generating new features, prefer:

* Multiple object color detection.
* Bounding box visualization.
* Contour-based detection.
* HSV calibration utilities.
* Saving detection results.
* Support for external camera devices.

Avoid introducing heavy frameworks unless explicitly requested.

#for more details, refer to the README.md file in the project repository.
