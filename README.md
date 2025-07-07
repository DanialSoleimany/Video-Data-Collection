
# Video Object Cropper Using YOLO

Extract cropped images of specific objects from a defined time interval of a video using a YOLO model. The script processes frames at a target FPS and organizes the cropped objects in folders by second and frame number.

---

## Features

* Process video between specified start and end times (e.g., 10:10 to 10:12)
* Extract frames at configurable frames-per-second (FPS)
* Detect objects using YOLO model (`ultralytics` package)
* Save cropped objects of your chosen class (e.g., `truck`, `car`) in organized folders
* Print real-time logs for progress monitoring

---

## Requirements

* Python 3.7+
* OpenCV
* Ultralytics YOLO (`pip install ultralytics`)

---

## Installation

```bash
pip install opencv-python ultralytics
```

---

## Usage

### 1. Prepare your files

* Video file (e.g., `path/to/your/video.mp4`)
* YOLO model weights file (e.g., `path/to/your/yolo-model.pt`)

### 2. Run the extraction script

```python
from your_script import extract_object_crops_from_video

extract_object_crops_from_video(
    video_path="path/to/your/video.mp4",
    model_path="path/to/your/yolo-model.pt",
    output_dir="path/to/output/folder",
    start_time_str="10:10",
    end_time_str="10:12",
    target_fps=1,
    target_class="truck"
)
```

---

## Parameters

| Parameter        | Description                                              | Example             |
| ---------------- | -------------------------------------------------------- | ------------------- |
| `video_path`     | Path to your input video file                            | `"videos/game.mp4"` |
| `model_path`     | Path to your YOLO model weights file                     | `"models/yolo.pt"`  |
| `output_dir`     | Directory to save cropped images                         | `"output/crops"`    |
| `start_time_str` | Start time (mm\:ss or hh\:mm\:ss) to begin processing    | `"10:10"`           |
| `end_time_str`   | End time (mm\:ss or hh\:mm\:ss) to stop processing       | `"10:12"`           |
| `target_fps`     | Number of frames to process per second in the time range | `1`                 |
| `target_class`   | Object class to detect and crop (must be in your model)  | `"truck"`           |

---

## Output Structure

```
output_dir/
 ├─ second_0/
 │   ├─ frame_0/
 │   │    ├─ truck_601_0.jpg
 │   │    └─ truck_601_1.jpg
 │   └─ frame_1/
 │        └─ truck_607_0.jpg
 └─ second_1/
     └─ frame_0/
          └─ truck_611_0.jpg
```

* `second_X` folders correspond to seconds since the start time
* `frame_Y` folders correspond to frames extracted per second
* Cropped images are named by class, frame number, and object index

---

## Notes

* Ensure the class name you provide (`target_class`) matches exactly with a class name supported by your YOLO model.
* Increase `target_fps` to extract more frames per second (at the cost of processing time).
* Make sure the model weights are compatible with the `ultralytics` YOLO package.

---
