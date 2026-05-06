"""
Road Profile Viewer - Interactive 2D Visualization
===================================================
Main entry point for the road profile viewer application.

This application visualizes a road profile with camera ray intersection
using an interactive Dash interface.
"""

from road_profile_viewer.visualization import create_dash_app


def main():
    """
    Main function to run the Dash application.
    """
    app = create_dash_app()
    print("Starting Road Profile Viewer...")
    print("Open your browser and navigate to: http://127.0.0.1:8050/")
    print("Press Ctrl+C to stop the server.")
    app.run(debug=True)


if __name__ == "__main__":
    main()
