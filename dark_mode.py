# dark_mode.py

def get_dark_mode_colors():
    return {
        "bg_color": "#2c1616",          # Very dark gray background
        "button_color": "#dd6e6e",      # Light red buttons
        "text_color": "#ffffff",        # White text
        "hover_bg_color": "#b05858",    # Dark red on hover
        "hover_text_color": "#ffffff",  # White text on hover
        "current_bottom_box_color": "#582c2c"  # Dark red for bottom box
    }

def get_light_mode_colors():
    return {
        "bg_color": "#ffecec",          # Light pink background
        "button_color": "#ffbaba",      # Medium pink buttons
        "text_color": "#663f3f",        # Dark pink text
        "hover_bg_color": "#663f3f",    # Dark pink on hover
        "hover_text_color": "#ffffff",  # White text on hover
        "current_bottom_box_color": "#ffd8d8"  # Light pink for bottom box
    }
