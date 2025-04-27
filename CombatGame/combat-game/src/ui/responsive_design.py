def set_responsive_layout(screen_width, screen_height):
    # Adjust layout based on screen size
    if screen_width < 600:  # Mobile
        return {
            'card_size': (100, 150),
            'font_size': 14,
            'button_size': (80, 40),
            'layout': 'vertical'
        }
    elif screen_width < 1200:  # Tablet
        return {
            'card_size': (150, 200),
            'font_size': 16,
            'button_size': (100, 50),
            'layout': 'horizontal'
        }
    else:  # Desktop
        return {
            'card_size': (200, 300),
            'font_size': 18,
            'button_size': (120, 60),
            'layout': 'grid'
        }

def toggle_dark_mode(is_dark_mode):
    # Change UI colors based on mode
    if is_dark_mode:
        return {
            'background_color': '#333333',
            'text_color': '#FFFFFF',
            'button_color': '#555555'
        }
    else:
        return {
            'background_color': '#FFFFFF',
            'text_color': '#000000',
            'button_color': '#DDDDDD'
        }