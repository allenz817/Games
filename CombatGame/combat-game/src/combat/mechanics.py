def calculate_damage(attacker_damage, defender_armor):
    """
    Calculate the damage dealt in combat
    :param attacker_damage: The attacker's damage value
    :param defender_armor: The defender's armor value
    :return: The actual damage dealt
    """
    return max(0, attacker_damage - defender_armor)

def is_game_over(player_health, ai_health):
    """
    Check if the game is over
    :param player_health: The player's current health
    :param ai_health: The AI's current health
    :return: True if the game is over, False otherwise
    """
    return player_health <= 0 or ai_health <= 0

def apply_card_effect(player, card, target=None):
    """
    Apply a card's effect to the player or target
    :param player: The player playing the card
    :param card: The card being played
    :param target: The target of the card effect (None for self-targeting)
    """
    effect = card.effect.lower()
    
    if "damage" in effect:
        # Extract damage value from the effect text
        try:
            damage_value = int(''.join(filter(str.isdigit, effect)))
            total_damage = player.damage + damage_value
            if target:
                actual_damage = calculate_damage(total_damage, target.armor)
                target.health -= actual_damage
                print(f"Card deals {actual_damage} damage! Target health: {target.health}")
        except ValueError:
            print("Could not parse damage value")
    
    elif "heal" in effect or "restore" in effect:
        # Extract healing value from the effect text
        try:
            heal_value = int(''.join(filter(str.isdigit, effect)))
            player.health += heal_value
            if player.health > 100:  # Assuming 100 is max health
                player.health = 100
            print(f"Healed for {heal_value}! Health: {player.health}")
        except ValueError:
            print("Could not parse healing value")
    
    elif "armor" in effect:
        # Extract armor value from the effect text
        try:
            armor_value = int(''.join(filter(str.isdigit, effect)))
            player.armor += armor_value
            print(f"Gained {armor_value} armor! Total armor: {player.armor}")
        except ValueError:
            print("Could not parse armor value")
    
    elif "mana" in effect:
        # Extract mana value from the effect text
        try:
            mana_value = int(''.join(filter(str.isdigit, effect)))
            player.mana.current += mana_value
            if player.mana.current > player.mana.max:
                player.mana.current = player.mana.max
            print(f"Gained {mana_value} mana! Current mana: {player.mana.current}")
        except ValueError:
            print("Could not parse mana value")
    
    elif "draw" in effect:
        # Extract card draw value from the effect text
        try:
            draw_value = int(''.join(filter(str.isdigit, effect)))
            print(f"Drawing {draw_value} cards")
        except ValueError:
            print("Could not parse card draw value")