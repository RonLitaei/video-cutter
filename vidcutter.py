import subprocess
import argparse
import os

def cut_video(input_file, start_time, end_time, output_file=None):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    if not output_file:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_cut{ext}"


    command = [
        'ffmpeg',
        '-ss', start_time,
        '-to', end_time,
        '-i', input_file,
        '-c', 'copy',
        '-y',
        output_file
    ]

    print(f"Running command: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        print(f"Success! Saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("Error: FFmpeg is not installed or not in system PATH.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut video quickly using FFmpeg without re-encoding.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("start", help="Start time (HH:MM:SS or seconds)")
    parser.add_argument("end", help="End time (HH:MM:SS or seconds)")
    parser.add_argument("-o", "--output", help="Path to output file (optional)")

    args = parser.parse_args()

    cut_video(args.input, args.start, args.end, args.output)