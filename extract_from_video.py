import os
import cv2
from ultralytics import YOLO

def time_to_seconds(time_str):
    """
    Converts time string in format mm:ss or hh:mm:ss to seconds.
    """
    parts = time_str.split(':')
    if len(parts) == 2:
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds
    elif len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError("Invalid time format. Use mm:ss or hh:mm:ss")

def extract_object_crops_from_video(
    video_path: str,
    model_path: str,
    output_dir: str,
    start_time_str: str,
    end_time_str: str,
    target_fps: int = 1,
    target_class: str = "truck"
):
    """
    Extracts and saves object crops from a video in a given time range using a YOLO model.

    Parameters:
    - video_path (str): Path to the input video.
    - model_path (str): Path to the YOLO model (.pt file).
    - output_dir (str): Directory where cropped images will be saved.
    - start_time_str (str): Start time in 'mm:ss' or 'hh:mm:ss' format.
    - end_time_str (str): End time in 'mm:ss' or 'hh:mm:ss' format.
    - target_fps (int): Number of frames to process per second.
    - target_class (str): Name of the class to crop (must match model's class names).
    """

    start_time_sec = time_to_seconds(start_time_str)
    end_time_sec = time_to_seconds(end_time_str)

    os.makedirs(output_dir, exist_ok=True)

    print(f"🔄 Loading model from: {model_path}")
    model = YOLO(model_path)

    print(f"📹 Opening video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Error opening video file!")
        return

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time_sec * video_fps)
    end_frame = int(end_time_sec * video_fps)
    frame_interval = int(video_fps / target_fps)

    frame_num = 0
    saved_count = 0

    print(f"🚀 Starting extraction from {start_time_str} to {end_time_str} at {target_fps} FPS...\n")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        if frame_num < start_frame:
            frame_num += 1
            continue
        if frame_num > end_frame:
            break

        if (frame_num - start_frame) % frame_interval == 0:
            seconds_since_start = (frame_num - start_frame) // int(video_fps)
            frame_in_second = ((frame_num - start_frame) % int(video_fps)) // frame_interval

            frame_folder = os.path.join(output_dir, f"second_{seconds_since_start}", f"frame_{frame_in_second}")
            os.makedirs(frame_folder, exist_ok=True)

            results = model(frame)[0]
            if results.boxes is not None:
                for i, box in enumerate(results.boxes):
                    cls_id = int(box.cls[0])
                    cls_name = model.names[cls_id]
                    if cls_name.lower() == target_class.lower():
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cropped = frame[y1:y2, x1:x2]
                        filename = os.path.join(frame_folder, f"{target_class}_{frame_num}_{i}.jpg")
                        cv2.imwrite(filename, cropped)
                        saved_count += 1
                        print(f"✅ Saved {filename}")

        frame_num += 1

    cap.release()
    print(f"\n🎉 Done! Total {saved_count} cropped images saved.")

