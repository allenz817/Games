def calculate_damage(attacker_damage, defender_armor):
    """Calculate the damage dealt by an attacker to a defender."""
    damage_dealt = max(0, attacker_damage - defender_armor)
    return damage_dealt

def is_game_over(player_health, opponent_health):
    """Determine if the game is over based on player and opponent health."""
    return player_health <= 0 or opponent_health <= 0

def apply_damage(health, damage):
    """Apply damage to health and return the new health value."""
    return max(0, health - damage)