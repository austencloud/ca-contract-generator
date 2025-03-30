# utils/themes.py
"""
Theme management utilities for the contract generator
"""

# Dictionary of available themes with their color schemes
THEMES = {
    "Cirque Aflame": {
        "primary_color": "#3a0ca3",  # Deep purple
        "secondary_color": "#f72585",  # Bright pink
        "accent_color": "#4cc9f0",  # Bright blue
        "text_color": "#333333",  # Dark gray
        "light_color": "#f8f9fa",  # Light gray
        "border_color": "#dee2e6",  # Border gray
        "highlight_color": "#7209b7",  # Light purple
        "deep_color": "#d00000",  # Deep red
        "banner_gradient": "linear-gradient(90deg, #001871, #7209b7, #d00000)",
        "header_gradient": "linear-gradient(135deg, var(--primary-color), var(--secondary-color))",
        "font_family": "'Montserrat', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    },
    "Elegant": {
        "primary_color": "#1a237e",  # Deep navy
        "secondary_color": "#c2185b",  # Burgundy
        "accent_color": "#00acc1",  # Teal
        "text_color": "#212121",  # Near black
        "light_color": "#f5f5f5",  # Off white
        "border_color": "#e0e0e0",  # Light gray
        "highlight_color": "#5c6bc0",  # Muted purple
        "deep_color": "#880e4f",  # Deep magenta
        "banner_gradient": "linear-gradient(90deg, #1a237e, #5c6bc0, #c2185b)",
        "header_gradient": "linear-gradient(135deg, var(--primary-color), var(--secondary-color))",
        "font_family": "'Georgia', 'Times New Roman', serif",
    },
    "Modern": {
        "primary_color": "#2e3b4e",  # Slate blue
        "secondary_color": "#ff595e",  # Coral
        "accent_color": "#ffca3a",  # Yellow
        "text_color": "#2b2d42",  # Dark blue-gray
        "light_color": "#fdfffc",  # Clean white
        "border_color": "#dee2e6",  # Light gray
        "highlight_color": "#06aed5",  # Bright blue
        "deep_color": "#ff595e",  # Coral
        "banner_gradient": "linear-gradient(90deg, #2e3b4e, #06aed5, #ff595e)",
        "header_gradient": "linear-gradient(135deg, var(--primary-color), var(--secondary-color))",
        "font_family": "'Roboto', 'Arial', sans-serif",
    },
    "Professional": {
        "primary_color": "#284b63",  # Dark blue
        "secondary_color": "#3c6e71",  # Teal
        "accent_color": "#d9d9d9",  # Light gray
        "text_color": "#353535",  # Dark gray
        "light_color": "#f9f9f9",  # Near white
        "border_color": "#d9d9d9",  # Light gray
        "highlight_color": "#353535",  # Dark gray
        "deep_color": "#284b63",  # Dark blue
        "banner_gradient": "linear-gradient(90deg, #284b63, #3c6e71, #757575)",
        "header_gradient": "linear-gradient(135deg, var(--primary-color), var(--secondary-color))",
        "font_family": "'Helvetica', 'Arial', sans-serif",
    },
    "Creative": {
        "primary_color": "#540d6e",  # Purple
        "secondary_color": "#ee4266",  # Pink
        "accent_color": "#ffd23f",  # Yellow
        "text_color": "#1e1e24",  # Near black
        "light_color": "#f8f7ff",  # Off white
        "border_color": "#d3d3d3",  # Light gray
        "highlight_color": "#3bceac",  # Mint
        "deep_color": "#0ead69",  # Green
        "banner_gradient": "linear-gradient(90deg, #540d6e, #ee4266, #ffd23f)",
        "header_gradient": "linear-gradient(135deg, var(--primary-color), var(--secondary-color))",
        "font_family": "'Poppins', 'Verdana', sans-serif",
    },
}


def get_available_themes():
    """Return a list of available theme names"""
    return list(THEMES.keys())


def get_theme_colors(theme_name):
    """Get the color scheme for a specific theme"""
    if theme_name in THEMES:
        return THEMES[theme_name]

    # Return default theme if requested theme doesn't exist
    return THEMES["Cirque Aflame"]


def get_css_variables(theme_name):
    """Generate CSS variables for a theme"""
    theme = get_theme_colors(theme_name)

    css_vars = ""
    for key, value in theme.items():
        if key != "font_family":
            css_vars += f"--{key}: {value};\n        "

    return css_vars
