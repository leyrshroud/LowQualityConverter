import subprocess
import argparse
import os
import sys


def find_ffmpeg():
    # Try system PATH
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 'ffmpeg'
    except FileNotFoundError:
        pass

    # Try common Windows paths
    common_paths = [
        r"C:\Program Files\DownloadHelper CoApp\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Data\chocolatey\bin\ffmpeg.exe",
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return f'"{path}"'
            
    return None


def convert_to_meme_quality(input_path, output_path, quality='medium', custom_config=None):
    # Converts a video to a low-quality 2000s meme style.
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        print("\n" + "="*60)
        print("ERROR: FFMPEG NOT FOUND")
        print("="*60)
        print("Reason: This script requires 'ffmpeg' to process video files, but it")
        print("        could not be found in the system PATH or common locations.")
        print("\nSolution: Please install ffmpeg. On Windows, you can do this by")
        print("          running the following command in PowerShell:")
        print("\n          winget install ffmpeg")
        print("\nNote: You may need to restart your terminal after installation.")
        print("="*60 + "\n")
        return

    # Define quality presets
    presets = {
        'low': {
            'res': '176x144',
            'v_bitrate': '30k',
            'a_bitrate': '8k',
            'fps': '8'
        },
        'medium': {
            'res': '320x240',
            'v_bitrate': '80k',
            'a_bitrate': '24k',
            'fps': '12'
        },
        'high': {
            'res': '480x360',
            'v_bitrate': '250k',
            'a_bitrate': '48k',
            'fps': '20'
        }
    }

    config = presets.get(quality, presets['medium'])
    
    # if provided custom config
    if custom_config:
        for key, value in custom_config.items():
            if value:
                config[key] = value

    command = f"{ffmpeg_path} -i \"{input_path}\" -vf \"fps={config['fps']},scale={config['res']}:flags=neighbor\" -vcodec libx264 -b:v {config['v_bitrate']} -maxrate {config['v_bitrate']} -bufsize 500k -acodec libmp3lame -b:a {config['a_bitrate']} -ar 22050 -ac 1 -y \"{output_path}\""

    print(f"Using ffmpeg at: {ffmpeg_path}")
    print(f"Converting '{input_path}' to '{output_path}' with {quality} quality...")
    print(f"Settings: {config['res']}, {config['fps']}fps, {config['v_bitrate']} video, {config['a_bitrate']} audio")

    try:
        subprocess.run(command, check=True, shell=True)
        print("\nSuccess! Your video is now properly ruined.")
    except subprocess.CalledProcessError as e:
        print(f"\nError during conversion: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="2000s Meme Video Quality Ruiner")
    parser.add_argument("input_pos", nargs='?', help="Path to input video file (positional)")
    parser.add_argument("-i", "--in", "--input", dest="input_flag", help="Path to input video file (flag)")
    parser.add_argument("-o", "--out", "--output", dest="output", help="Path to output video file (default: input_meme.mp4)")
    parser.add_argument("-q", "--quality", choices=['low', 'medium', 'high'], default='medium', 
                        help="Quality level preset (default: medium)")
    parser.add_argument("--res", help="Custom resolution (e.g., 320x240)")
    parser.add_argument("--fps", help="Custom framerate (e.g., 12)")
    parser.add_argument("--vbit", help="Custom video bitrate (e.g., 100k)")
    parser.add_argument("--abit", help="Custom audio bitrate (e.g., 32k)")

    args = parser.parse_args()

    input_file = args.input_flag if args.input_flag else args.input_pos
    output_file = args.output

    if not input_file:
        parser.print_help()
        sys.exit(1)

    if not output_file:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_out.mp4"

    custom = {
        'res': args.res,
        'fps': args.fps,
        'v_bitrate': args.vbit,
        'a_bitrate': args.abit
    }

    convert_to_meme_quality(input_file, output_file, args.quality, custom)
