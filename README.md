# 📸 Instagram-style Filters Camera

A powerful, real-time camera filter application built with Python, OpenCV, and PySide6. Apply 94 unique filters to your live webcam feed instantly.

## ✨ Key Features

*   **94 Unique Filters** across 14 categories:
    *   **Instagram Classics**: Clarendon, Gingham, Juno, Lark, Reyes, Aden, Brooklyn, Earlybird, Hudson, Inkwell, Lo-Fi, Nashville, Rise, Valencia, Walden, Amaro, Brannan, Hefe, Toaster, Maven, Vesper, Chrome
    *   **Classic Styles**: 1977, Kelvin, Slumber, Sutro, Moon (B&W), X-Pro II, Mayfair
    *   **Retro & Vintage**: Sepia, Polaroid, Vintage, Retro 80s, Lomo
    *   **Cinematic**: Teal-Orange, Cross Process, Bleach Bypass, Dramatic, Noir, Tokyo Nights
    *   **Artistic**: Sketch, Cartoon, Pop Art, Emboss
    *   **Tech & Glitch**: Cyberpunk, Thermal, Infrared, Night Vision, Glitch, RGB Split, Digital Corrupt, Pixelate, TV Static
    *   **Color Moods**: Pastel Dream, Cotton Candy, Sunset Vibes, Neon Glow, Moody Blues, Soft Focus
    *   **Nature Themes**: Arctic, Desert, Forest, Fire, Ice
    *   **Trendy Colors**: Lavender, Mint, Peach, Rose Gold
    *   **Seasonal**: Summer, Autumn, Winter, Spring, Blue Hour
    *   **Distortions**: Mirror, Fisheye, Swirl, Bulge, Pinch, Ripple, Twist, Perspective Tilt
    *   **Blurs**: Motion Blur, Radial Blur, Tilt Shift
    *   **Reflections**: Vertical Flip, Quad Mirror, Glass Window
    *   **Light & Texture**: Bloom, Light Leak, Negative, Posterize, Film Dust
*   **Real-time Processing**: Effects applied live at ~30 fps.
*   **Intensity Control**: Slider to blend filter strength (0–100%).
*   **Compare Mode**: Hold "Hold to Compare" to preview the unfiltered feed.
*   **Snapshot**: Capture timestamped images with "Say Cheese 📸".
*   **Video Recording**: Record filtered video with the "Record" button.
*   **Mirror Mode**: Toggle horizontal camera flip.
*   **Watermark**: Optional "By- Chandan Raj" overlay toggle.
*   **Flash Effect**: Visual flash animation on snapshot.
*   **Random Filter**: One-click random filter picker.

## 🛠️ Installation

### Prerequisites

Python 3.8 or newer is required.

### Install Dependencies

```bash
pip install opencv-python numpy PySide6
```

## 🚀 Usage

1.  **Run the Application**:

    ```bash
    python main.py
    ```

2.  **Controls**:

    | Action | How |
    |---|---|
    | Select a filter | Click a name in the filter list, or use **Prev / Next** buttons |
    | Adjust strength | Drag the **Intensity** slider |
    | Take a photo | Click **"Say Cheese 📸"** → saved to `output/` |
    | Record video | Click **"Record"** to start/stop → saved to `output/` |
    | Compare original | Click and hold **"Hold to Compare"** |
    | Random filter | Click **"Select Random Filter"** |
    | Open saved files | Click **"Open Save Folder"** |

## 📂 Project Structure

```
filters-camera/
├── main.py          # Entry point — configures app style and launches the window
├── ui.py            # PySide6 UI, camera capture loop, and user interaction logic
├── utils.py         # Shared image helpers (clamp, adjust_brightness_contrast, etc.)
├── filters/
│   ├── __init__.py     # Assembles the full FILTERS list
│   ├── artistic.py     # Sketch, Cartoon, Pop Art, Emboss
│   ├── beauty.py       # Soft Skin
│   ├── blurs.py        # Motion Blur, Radial Blur, Tilt Shift
│   ├── color_moods.py  # Pastel Dream, Neon Glow, Moody Blues, etc.
│   ├── distortion.py   # Fisheye, Swirl, Bulge, Ripple, Twist, etc.
│   ├── instagram.py    # Instagram-style classics
│   ├── light.py        # Bloom, Light Leak, Negative, Posterize, Film Dust
│   ├── reflections.py  # Vertical Flip, Quad Mirror, Glass Window
│   ├── retro.py        # Sepia, Polaroid, 1977, Kelvin, Lomo, etc.
│   ├── tech.py         # Cyberpunk, Thermal, Glitch, RGB Split, etc.
│   └── utils.py        # Filter-specific helpers
└── output/          # Saved snapshots and recordings
```

## 👤 Credits

**Developer**: Chandan Raj

---
*Made with ❤️*
