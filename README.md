# Video Cutter

A simple Python script to quickly cut/trim video files using FFmpeg without re-encoding. This preserves the original video quality and processes files much faster than traditional video editors.

## Features

- Fast video cutting using stream copy (no re-encoding)
- Preserves original video quality
- Supports all video formats that FFmpeg supports
- Simple command-line interface
- Automatic output filename generation

## Prerequisites

- Python 3.x
- FFmpeg installed and available in system PATH

### Installing FFmpeg

**Windows:**
- winget install "FFmpeg (Essentials Build)"  

## Usage

```bash
python video_cutter.py <input_file> <start_time> <end_time> [-o output_file]
```

### Arguments

- `input_file` - Path to the input video file
- `start_time` - Start time in format `HH:MM:SS` or seconds (e.g., `00:01:30` or `90`)
- `end_time` - End time in format `HH:MM:SS` or seconds (e.g., `00:05:00` or `300`)
- `-o, --output` - (Optional) Path to output file. If not specified, adds `_cut` suffix to input filename

### Examples

Cut from 1 minute 30 seconds to 5 minutes:
```bash
python video_cutter.py video.mp4 00:01:30 00:05:00
```

Specify custom output file:
```bash
python video_cutter.py video.mp4 00:01:30 00:05:00 -o highlight.mp4
```

## License

MIT License - feel free to use and modify as needed.
