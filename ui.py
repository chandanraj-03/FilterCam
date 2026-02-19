import cv2
import numpy as np
import time
import sys
import os
import random
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                QHBoxLayout, QPushButton, QLabel, QListWidget, 
                                QGroupBox, QSplitter, QCheckBox, QSlider, QFrame, QMessageBox)
from PySide6.QtCore import QTimer, Qt, QUrl
from PySide6.QtGui import QImage, QPixmap, QDesktopServices
from filters import FILTERS

class FilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Instagram-style Filters Camera ({len(FILTERS)} Filters!)")
        self.setGeometry(100, 100, 1200, 700)
        
        self.output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.cap = None
        self.camera_available = False
        self.init_camera()
        
        self.current_filter_idx = 0
        self.current_frame = None
        self.filtered_frame = None
        
        self.mirror = True
        self.intensity = 1.0
        self.compare_mode = False
        self.watermark_enabled = False
        self.flash_opacity = 0.0
        
        self.is_recording = False
        self.video_writer = None
        
        self.setup_ui()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
    
    def init_camera(self):
        backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]
        indices = [0, 1, 2]
        
        for backend in backends:
            for idx in indices:
                try:
                    print(f"Trying camera {idx} with backend {backend}...")
                    cap = cv2.VideoCapture(idx, backend)
                    
                    if cap.isOpened():
                        ret, frame = cap.read()
                        if ret and frame is not None:
                            print(f"✓ Camera {idx} opened successfully with backend {backend}")
                            self.cap = cap
                            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                            self.camera_available = True
                            return
                    cap.release()
                except Exception as e:
                    print(f"Failed to open camera {idx} with backend {backend}: {e}")
                    
        print("⚠ No camera available. Will use placeholder image.")
        self.camera_available = False
        
    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(2)
        main_layout.addWidget(splitter)
        
        video_widget = QWidget()
        video_layout = QVBoxLayout(video_widget)
        video_layout.setContentsMargins(0, 0, 0, 0)
        video_layout.setSpacing(10)
        
        self.video_label = QLabel()
        self.video_label.setMinimumSize(640, 480)
        self.video_label.setStyleSheet("border: 2px solid #3e3e42; background-color: #000; border-radius: 8px;")
        self.video_label.setAlignment(Qt.AlignCenter)
        video_layout.addWidget(self.video_label)
        
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("padding: 5px; font-size: 13px; color: #888;")
        self.status_label.setAlignment(Qt.AlignCenter)
        video_layout.addWidget(self.status_label)
        
        self.flash_overlay = QWidget(self.video_label)
        self.flash_overlay.setStyleSheet("background-color: white;")
        self.flash_overlay.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.flash_overlay.hide()
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.btn_retry = QPushButton("🔄 Retry Camera")
        self.btn_retry.setObjectName("btn_retry")
        self.btn_retry.setCursor(Qt.PointingHandCursor)
        self.btn_retry.clicked.connect(self.retry_camera)
        button_layout.addWidget(self.btn_retry)
        
        self.btn_prev = QPushButton("◀ Previous")
        self.btn_prev.setCursor(Qt.PointingHandCursor)
        self.btn_prev.clicked.connect(self.prev_filter)
        button_layout.addWidget(self.btn_prev)
        
        self.btn_save = QPushButton("Say Cheese 📸")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setCursor(Qt.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_screenshot)
        button_layout.addWidget(self.btn_save)

        self.btn_record = QPushButton("⏺ Record")
        self.btn_record.setObjectName("btn_record")
        self.btn_record.setCursor(Qt.PointingHandCursor)
        self.btn_record.clicked.connect(self.toggle_recording)
        button_layout.addWidget(self.btn_record)
        
        self.btn_next = QPushButton("Next ▶")
        self.btn_next.setCursor(Qt.PointingHandCursor)
        self.btn_next.clicked.connect(self.next_filter)
        button_layout.addWidget(self.btn_next)
        
        video_layout.addLayout(button_layout)
        
        extra_controls_layout = QHBoxLayout()
        
        self.btn_compare = QPushButton("👁 Hold to Compare")
        self.btn_compare.setCursor(Qt.PointingHandCursor)
        self.btn_compare.pressed.connect(self.start_compare)
        self.btn_compare.released.connect(self.stop_compare)
        extra_controls_layout.addWidget(self.btn_compare)
        
        self.btn_open_folder = QPushButton("📂 Open Save Folder")
        self.btn_open_folder.setCursor(Qt.PointingHandCursor)
        self.btn_open_folder.clicked.connect(self.open_save_folder)
        extra_controls_layout.addWidget(self.btn_open_folder)

        self.btn_help = QPushButton("ℹ️ Help")
        self.btn_help.setCursor(Qt.PointingHandCursor)
        self.btn_help.clicked.connect(self.show_help)
        extra_controls_layout.addWidget(self.btn_help)
        
        video_layout.addLayout(extra_controls_layout)
        
        splitter.addWidget(video_widget)
        
        filter_widget = QWidget()
        filter_layout = QVBoxLayout(filter_widget)
        filter_layout.setContentsMargins(10, 0, 0, 0)
        
        filter_group = QGroupBox(f"Available Filters ({len(FILTERS)})")
        filter_group_layout = QVBoxLayout()
        filter_group_layout.setContentsMargins(10, 25, 10, 10)
        
        self.filter_list = QListWidget()
        for i, (name, _) in enumerate(FILTERS):
            self.filter_list.addItem(f"{i+1}. {name}")
        self.filter_list.setCurrentRow(0)
        self.filter_list.currentRowChanged.connect(self.on_filter_selected)
        filter_group_layout.addWidget(self.filter_list)
        
        controls_group = QGroupBox("Adjustments")
        controls_layout = QVBoxLayout()
        
        self.check_mirror = QCheckBox("Mirror Camera")
        self.check_mirror.setChecked(True)
        self.check_mirror.stateChanged.connect(self.toggle_mirror)
        controls_layout.addWidget(self.check_mirror)
        
        self.check_watermark = QCheckBox("Add Watermark")
        self.check_watermark.setChecked(False)
        self.check_watermark.stateChanged.connect(self.toggle_watermark)
        controls_layout.addWidget(self.check_watermark)
        
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(QLabel("Intensity:"))
        self.slider_intensity = QSlider(Qt.Horizontal)
        self.slider_intensity.setRange(0, 100)
        self.slider_intensity.setValue(100)
        self.slider_intensity.valueChanged.connect(self.set_intensity)
        slider_layout.addWidget(self.slider_intensity)
        controls_layout.addLayout(slider_layout)
        
        action_layout = QHBoxLayout()
        self.btn_random = QPushButton("Select Random Filter")
        self.btn_random.clicked.connect(self.random_filter)
        action_layout.addWidget(self.btn_random)
        
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.clicked.connect(self.reset_filter)
        action_layout.addWidget(self.btn_reset)
        controls_layout.addLayout(action_layout)
        
        controls_group.setLayout(controls_layout)
        filter_group_layout.addWidget(controls_group)
        
        filter_group.setLayout(filter_group_layout)
        filter_layout.addWidget(filter_group)
        
        splitter.addWidget(filter_widget)
        
        splitter.setSizes([840, 360])
        
    def update_frame(self):
        if not self.camera_available or self.cap is None or not self.cap.isOpened():
            self.show_placeholder()
            return
            
        ret, frame = self.cap.read()
        if not ret or frame is None:
            self.show_placeholder()
            return
        
        if self.mirror:
            frame = cv2.flip(frame, 1)
        self.current_frame = frame.copy()
        
        if self.compare_mode:
            display_frame = frame.copy()
            name = "Original (Compare)"
            
            cv2.putText(display_frame, "COMPARE", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            name, filter_fn = FILTERS[self.current_filter_idx]
            filtered = filter_fn(frame.copy())
            
            if self.intensity < 1.0:
                display_frame = cv2.addWeighted(frame, 1.0 - self.intensity, filtered, self.intensity, 0)
            else:
                display_frame = filtered
                
        if self.watermark_enabled:
            self._apply_watermark(display_frame)

        self.filtered_frame = display_frame.copy()
        
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(display_frame)
            cv2.putText(display_frame, "REC...", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255), 2, cv2.LINE_AA)

        if self.flash_opacity > 0:
            overlay = np.full_like(display_frame, 255)
            display_frame = cv2.addWeighted(display_frame, 1.0 - self.flash_opacity, overlay, self.flash_opacity, 0)
            self.flash_opacity = max(0, self.flash_opacity - 0.1)
        
        rgb_image = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.video_label.setPixmap(scaled_pixmap)
        
        self.flash_overlay.resize(self.video_label.size())
        
        self.status_label.setText(f"📷 Filter: {name} ({self.current_filter_idx + 1}/{len(FILTERS)}) | Intensity: {int(self.intensity*100)}%")

    def _apply_watermark(self, frame):
        """Apply watermark to the given frame"""
        text = "By- Chandan Raj"
        h, w = frame.shape[:2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.4
        thickness = 1
        (text_w, text_h), _ = cv2.getTextSize(text, font, scale, thickness)
        
        x = w - text_w - 20
        y = h - 20
        
        overlay = frame.copy()
        
        cv2.putText(overlay, text, (x+2, y+2), font, scale, (0, 0, 0), thickness)
        cv2.putText(overlay, text, (x, y), font, scale, (255, 255, 255), thickness)
        
        alpha = 0.7
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    
    def show_placeholder(self):
        placeholder = np.zeros((480, 640, 3), dtype=np.uint8)
        placeholder[:] = (40, 40, 40)
        
        text = "Camera Not Available"
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(text, font, 1.2, 2)[0]
        text_x = (640 - text_size[0]) // 2
        text_y = (480 + text_size[1]) // 2
        cv2.putText(placeholder, text, (text_x, text_y - 30), font, 1.2, (255, 255, 255), 2)
        
        text2 = "Click 'Retry Camera' to reconnect"
        text_size2 = cv2.getTextSize(text2, font, 0.7, 1)[0]
        text_x2 = (640 - text_size2[0]) // 2
        cv2.putText(placeholder, text2, (text_x2, text_y + 20), font, 0.7, (180, 180, 180), 1)
        
        rgb_image = cv2.cvtColor(placeholder, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.video_label.setPixmap(scaled_pixmap)
        self.status_label.setText("❌ Camera not available - Click 'Retry Camera' button")
    
    def retry_camera(self):
        if self.cap is not None:
            self.cap.release()
        self.status_label.setText("🔄 Attempting to reconnect camera...")
        QApplication.processEvents()
        self.init_camera()
        if self.camera_available:
            self.status_label.setText("✅ Camera reconnected successfully!")
        else:
            self.status_label.setText("❌ Failed to connect camera. Check if another app is using it.")
        
    def prev_filter(self):
        self.current_filter_idx = (self.current_filter_idx - 1) % len(FILTERS)
        self.filter_list.setCurrentRow(self.current_filter_idx)
        
    def next_filter(self):
        self.current_filter_idx = (self.current_filter_idx + 1) % len(FILTERS)
        self.filter_list.setCurrentRow(self.current_filter_idx)
        
    def on_filter_selected(self, row):
        if row >= 0:
            self.current_filter_idx = row
            
    def toggle_mirror(self, state):
        self.mirror = (state == Qt.Checked.value)
        
    def toggle_watermark(self, state):
        self.watermark_enabled = (state == Qt.Checked.value)
        
    def set_intensity(self, value):
        self.intensity = value / 100.0
        
    def start_compare(self):
        self.compare_mode = True
        
    def stop_compare(self):
        self.compare_mode = False
        
    def random_filter(self):
        self.current_filter_idx = random.randint(0, len(FILTERS) - 1)
        self.filter_list.setCurrentRow(self.current_filter_idx)
        
    def reset_filter(self):
        self.current_filter_idx = 0
        self.filter_list.setCurrentRow(0)
        self.slider_intensity.setValue(100)
        self.intensity = 1.0

    def open_save_folder(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.output_dir))
        
    def flash_screen(self):
        self.flash_opacity = 0.8
            
    def save_screenshot(self):
        if self.filtered_frame is not None:
            save_img = self.filtered_frame.copy()
            
            name, _ = FILTERS[self.current_filter_idx]
            filename = f"filter_{name.replace(' ', '_').replace('/', '-').replace('(', '').replace(')', '')}_{int(time.time())}.png"
            filepath = os.path.join(self.output_dir, filename)
            cv2.imwrite(filepath, save_img)
            
            self.flash_screen()
            self.status_label.setText(f"✅ Saved: {filename}")
            print(f"Screenshot saved: {filepath}")
        
    def show_help(self):
        """Show help dialog with project info"""
        help_text = (
            "<h2>📸 Filters Camera</h2>"
            "<p>A powerful, real-time camera filter application built with Python, OpenCV, and PySide6. Feature-rich and easy to use, it brings Instagram-like filters to your desktop webcam.</p>"
            "<p></p>"
            "<h3>✨ Key Features:</h3>"
            "<ul>"
            f"<li><b>{len(FILTERS)} Unique Filters:</b> Choose from a wide variety of effects.</li>"
            "<li><b>Real-time Processing:</b> See effects instantly on your camera feed.</li>"
            "<li><b>Intensity Control:</b> Adjust filter strength with the slider.</li>"
            "<li><b>Compare Mode:</b> Hold 'Compare' to see the original image.</li>"
            "<li><b>Snapshots:</b> Save high-quality images with timestamps.</li>"
            "<li><b>Watermark:</b> Add watermark to the image.</li>"
            "<li><b>Recording:</b> Record video with filters.</li>"
            "<li><b>Reset:</b> Reset the filter to original.</li>"
            "<li><b>Random:</b> Pick a random filter.</li>"
            "</ul>"
            
            "<h3>🎮 Controls:</h3>"
            "<ul>"
            "<li><b>Prev/Next:</b> Cycle through filters.</li>"
            "<li><b>Save:</b> Capture the current frame.</li>"
            "<li><b>Mirror:</b> Flip the camera feed horizontally.</li>"
            "<li><b>Random:</b> Pick a surprise filter!</li>"
            "<li><b>Intensity:</b> Adjust filter strength.</li>"
            "<li><b>Compare:</b> Hold to see original image.</li>"
            "<li><b>Snapshot:</b> Save high-quality images.</li>"
            "<li><b>Watermark:</b> Add watermark to the image.</li>"
            "<li><b>Recording:</b> Record video with filters.</li>"
            "</ul>"
            
            "<hr>"
            "<p><i>Made with ❤️ by <b>Chandan Raj</b></i></p>"
        )
        
        QMessageBox.about(self, "About Project", help_text)

    def toggle_recording(self):
        if not self.is_recording:
            if self.cap is None or not self.cap.isOpened():
                self.status_label.setText("❌ Cannot record: Camera not available")
                return

            name, _ = FILTERS[self.current_filter_idx]
            filename = f"video_{name.replace(' ', '_').replace('/', '-').replace('(', '').replace(')', '')}_{int(time.time())}.avi"
            filepath = os.path.join(self.output_dir, filename)
            
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            fps = 20.0
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            try:
                self.video_writer = cv2.VideoWriter(filepath, fourcc, fps, (width, height))
                if not self.video_writer.isOpened():
                     self.status_label.setText("❌ Failed to start video writer")
                     self.video_writer = None
                     return
                     
                self.is_recording = True
                self.btn_record.setText("⏹ Stop Recording")
                self.btn_record.setStyleSheet("background-color: #cf6679; color: black; border: 1px solid #cf6679;")
                self.status_label.setText(f"🔴 Recording: {filename}")
                print(f"Started recording: {filepath}")
                
            except Exception as e:
                print(f"Error starting recording: {e}")
                self.status_label.setText(f"❌ Error: {e}")
                
        else:
            self.is_recording = False
            if self.video_writer is not None:
                self.video_writer.release()
                self.video_writer = None
            
            self.btn_record.setText("⏺ Record")
            self.btn_record.setStyleSheet("")
            self.status_label.setText("✅ Video Saved!")
            print("Stopped recording")

    def closeEvent(self, event):
        if self.is_recording and self.video_writer is not None:
            self.video_writer.release()
        if self.cap is not None:
            self.cap.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = FilterApp()
    window.show()
    sys.exit(app.exec())

