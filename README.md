## ✨ Info
Initially this project was created to capture the **"2000s meme vibe"**-those low-resolution, heavily compressed videos that dominated the early web. Whether you want to recreate a classic "potato quality" video or just feel some nostalgia, this tool is for you.

## 🚀 Features
- **Intentionally Low Quality**: Reduces resolution and bitrate to hit that sweet spot of degradation.
- **Nearest Neighbor Scaling**: Keeps pixels sharp (and blocky) instead of blurring them.
- **Audio "Crunch"**: Lowers audio bitrate and sample rate for that authentic compressed sound.
- **Presets**: Choose between `low`, `medium`, and `high` quality (all of which are technically "bad").

## 🛠️ Prerequisites
This script requires **FFmpeg** to be installed on your system.
- **Windows**: `winget install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### 📖 Usage
Run the script using Python:

```bash
python converter.py input_video.mp4 -q medium
```

### Options:
- `input`: Path to your high-quality video.
- `-o`, `--output`: Path to the output file (default: `input_out.mp4`).
- `-q`, `--quality`: Preset quality level (`low`, `medium`, `high`).
- `--res`: Custom resolution (e.g., `160x120`).
- `--fps`: Custom framerate (e.g., `8`).
- `--vbit`: Custom video bitrate (e.g., `50k`).
- `--abit`: Custom audio bitrate (e.g., `16k`).

### Example (Maximum "Potato" Quality):
```bash
python converter.py my_video.mp4 -q low --fps 5
```

## 📜 Quality Presets
| Preset | Resolution | FPS | Video Bitrate | Audio Bitrate |
| :--- | :--- | :--- | :--- | :--- |
| low | 176x144 | 8 | 30k | 8k |
| medium | 320x240 | 12 | 80k | 24k |
| high | 480x360 | 20 | 250k | 48k |

