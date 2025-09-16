"""
Mouse Position Tracker - Prints cursor position on right-click

Requirements:
    pip install pynput

Usage:
    Run the script and right-click anywhere on screen to see coordinates.
    Press Ctrl+C or Esc key to exit.
"""

from pynput import mouse, keyboard
import threading
import time

class MousePositionTracker:
    def __init__(self):
        self.running = True
        self.click_count = 0

    def on_click(self, x, y, button, pressed):
        """Handle mouse click events"""
        if button == mouse.Button.right and pressed:
            self.click_count += 1
            print(f"Right-click #{self.click_count}: Position (y={y}, x={x})")

    def on_key_press(self, key):
        """Handle keyboard events to exit"""
        try:
            if key == keyboard.Key.esc:
                print("\nEsc pressed. Stopping mouse tracker...")
                self.stop()
        except AttributeError:
            pass

    def on_key_combination(self):
        """Handle Ctrl+C combination"""
        print("\nCtrl+C detected. Stopping mouse tracker...")
        self.stop()

    def stop(self):
        """Stop the tracker"""
        self.running = False

    def start(self):
        """Start the mouse position tracker"""
        print("Mouse Position Tracker Started!")
        print("- Right-click anywhere to see cursor position (y, x)")
        print("- Press 'Esc' key or 'Ctrl+C' to exit")
        print("- Waiting for right-clicks...\n")

        # Set up mouse listener
        mouse_listener = mouse.Listener(on_click=self.on_click)
        mouse_listener.start()

        # Set up keyboard listener for exit
        keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        keyboard_listener.start()

        # Set up Ctrl+C handler
        with keyboard.GlobalHotKeys({'<ctrl>+c': self.on_key_combination}):
            try:
                # Keep the main thread alive
                while self.running:
                    time.sleep(0.1)

            except KeyboardInterrupt:
                print("\nKeyboardInterrupt received. Stopping...")
                self.stop()

        # Clean up
        mouse_listener.stop()
        keyboard_listener.stop()
        print("Mouse tracker stopped. Goodbye!")

# Alternative simpler version using just mouse events
def simple_mouse_tracker():
    """Simplified version - tracks only mouse events"""
    print("Simple Mouse Position Tracker")
    print("Right-click anywhere to see position. Press Ctrl+C to exit.\n")

    click_count = 0

    def on_click(x, y, button, pressed):
        nonlocal click_count
        if button == mouse.Button.right and pressed:
            click_count += 1
            print(f"Right-click #{click_count}: Position (y={y}, x={x})")

    # Start mouse listener
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nStopping tracker...")

# Version with additional features
def advanced_mouse_tracker():
    """Advanced version with more features"""
    print("Advanced Mouse Position Tracker")
    print("Features:")
    print("- Right-click: Show position")
    print("- Left-click: Show position (optional)")
    print("- Press 'Esc' to exit")
    print("- Press 'r' to reset counter\n")

    click_count = 0
    show_left_clicks = False  # Set to True if you want left-click positions too

    def on_click(x, y, button, pressed):
        nonlocal click_count

        if pressed:  # Only on press, not release
            if button == mouse.Button.right:
                click_count += 1
                print(f"RIGHT-CLICK #{click_count}: Position (y={y}, x={x})")

            elif button == mouse.Button.left and show_left_clicks:
                click_count += 1
                print(f"LEFT-CLICK #{click_count}: Position (y={y}, x={x})")

    def on_key_press(key):
        nonlocal click_count

        if key == keyboard.Key.esc:
            print("\nExiting...")
            return False  # Stop listener

        try:
            if key.char == 'r':
                click_count = 0
                print("Counter reset!")
        except AttributeError:
            pass

    # Start listeners
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_key_press)

    mouse_listener.start()
    keyboard_listener.start()

    try:
        keyboard_listener.join()
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        mouse_listener.stop()

if __name__ == "__main__":
    # Choose which version to run
    #print("Choose tracker version:")
    #print("1. Full-featured tracker (recommended)")
    #print("2. Simple tracker")
    #print("3. Advanced tracker")

    try:
        #choice = input("\nEnter choice (1-3) or press Enter for default [1]: ").strip()
        choice = 3

        if choice == "2":
            simple_mouse_tracker()
        elif choice == "3":
            advanced_mouse_tracker()
        else:
            # Default: full-featured tracker
            tracker = MousePositionTracker()
            tracker.start()

    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have installed pynput:")
        print("pip install pynput")