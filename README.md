

# 📦 Data Collection from Video using YOLO

Extract cropped images of specific objects from a defined time interval of a video using a YOLO model.
The script processes frames at a target FPS and organizes the cropped objects in folders by **second** and **frame number**.

---

## ✅ Features

* ⏱️ Process video between specified start and end times (e.g., `10:10` to `10:12`)
* 🎞️ Extract frames at a configurable frames-per-second (FPS)
* 🧠 Detect objects using YOLO (via the `ultralytics` package)
* 🖼️ Save cropped images of your target class (e.g., `"car"`)
* 📂 Organized output: Crops are saved per second/frame in nested folders
* 📢 Real-time progress printed to the console

---

## 🔧 Requirements

* Python 3.7+
* OpenCV (`cv2`)
* [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) (`pip install ultralytics`)

---

## 📦 Installation

```bash
pip install opencv-python ultralytics
```

---

## 🚀 Usage

### 1. Prepare Your Files

* 🎥 Your video file (e.g., `path/to/your/video.mp4`)
* 🧠 YOLO model file (`.pt`), trained or pre-trained (e.g., `path/to/your/yolo-model.pt`)

### 2. Run the Extraction Script

```python
from extract_from_video import extract_object_crops_from_video

extract_object_crops_from_video(
    video_path="path/to/your/video.mp4",
    model_path="path/to/your/yolo-model.pt",
    output_dir="path/to/output/folder",
    start_time_str="10:10",
    end_time_str="10:12",
    target_fps=1,
    target_class="car"
)
```

---

## ⚙️ Parameters

| Parameter        | Description                                            | Example             |
| ---------------- | ------------------------------------------------------ | ------------------- |
| `video_path`     | Path to your input video file                          | `"videos/game.mp4"` |
| `model_path`     | Path to your YOLO model weights                        | `"models/yolo.pt"`  |
| `output_dir`     | Directory where cropped images will be saved           | `"output/crops"`    |
| `start_time_str` | Start time in `mm:ss` or `hh:mm:ss` format             | `"10:10"`           |
| `end_time_str`   | End time in `mm:ss` or `hh:mm:ss` format               | `"10:12"`           |
| `target_fps`     | Number of frames to extract per second                 | `1`                 |
| `target_class`   | Class name of the object to crop (must exist in model) | `"car"`             |

---

## 📁 Output Structure

```
output_dir/
 ├─ second_0/
 │   ├─ frame_0/
 │   │    ├─ car_601_0.jpg
 │   │    └─ car_601_1.jpg
 │   └─ frame_1/
 │        └─ car_607_0.jpg
 └─ second_1/
     └─ frame_0/
          └─ car_611_0.jpg
```

* `second_X`: Second offset from the start time
* `frame_Y`: Frame index within that second
* Filenames follow pattern: `{class}_{frame_number}_{object_index}.jpg`

---

## 📝 Notes

* ✅ Make sure your `target_class` (like `"car"`) exactly matches one of the class names used by your YOLO model.
* ⚡ Increase `target_fps` if you want more frequent frame sampling.
* 📚 Your YOLO model must be compatible with the `ultralytics` YOLO API (v8+).
* 🧪 Use this method to prepare datasets for training or evaluation tasks.

---

اگر مایل باشی می‌تونم نسخه فارسی این README رو هم برات بنویسم یا فایل `.md` آماده دانلود بسازم.
