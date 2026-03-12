import LiteEFG as efg
import os


def process_game_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    try:
        # Load the environment
        env = efg.FileEnv(file_path, traverse_type="Enumerate")
        print("--------------------------------")
        print(f"SUCCESS: {file_path} loaded successfully!")
        print("--------------------------------")

    except Exception as e:
        print("--------------------------------")
        print("FAILURE: Could not process the game tree.")
        print(f"Error Details: {e}")
        print("--------------------------------")


if __name__ == "__main__":
    # Specify your game file name here
    # target_file = "blind_coin_match.game"
    # target_file = "card_game_3level.game"
    # target_file = "coin_match.game"
    # target_file = "known_good.game" #--------------------Does not work!! Segmentation Fault 11
    # target_file = "matching_pennies.game" #--------------------Does not work!! Segmentation Fault 11
    # target_file = "rps.game"
    # --------------------Does not work!! Segmentation Fault 11
    target_file = "sam_sead.game"
    # target_file = "simple_game.game"
    # target_file = "test.game"  # --------------------Does not work!! Segmentation Fault 11
    process_game_file(target_file)
