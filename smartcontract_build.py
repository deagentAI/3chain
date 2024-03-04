import os

# Path to your Visual Studio Code executable
VSCODE_PATH = "code"

def launch_smart_contract_template(contract_type):
    # Define the directory where your smart contract templates are stored
    templates_directory = "smart_contracts"

    # Map contract types to their corresponding template filenames
    template_mapping = {
        "ERC20": "ERC20.sol",
        "ERC721": "ERC721.sol",
        "ERC1155": "ERC1155.sol"
    }

    if contract_type in template_mapping:
        template_filename = template_mapping[contract_type]
        template_path = os.path.join(templates_directory, template_filename)

        # Launch Visual Studio Code with the smart contract template
        os.system(f"{VSCODE_PATH} {template_path}")
        return "Smart contract template launched in Visual Studio Code. You can start editing now!"
    else:
        return "Invalid contract type. Please choose a valid contract type."

# Prompt the user to select the contract type
def prompt_contract_type():
    while True:
        print("Available contract types:")
        print("1. ERC20")
        print("2. ERC721")
        print("3. ERC1155")
        print("0. Quit")

        user_input = input("Ella: Please enter the corresponding number: ")

        if user_input == "0":
            return None  # Return None to indicate going back to the previous menu

        if user_input.isdigit():
            index = int(user_input) - 1
            contract_types = ["ERC20", "ERC721", "ERC1155"]

            if 0 <= index < len(contract_types):
                return contract_types[index]
            else:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")

# Main entry point of the script
def main():
    while True:
        contract_type = prompt_contract_type()

        if contract_type is None:
            # User selected to go back to the previous menu
            break  # Exit the loop and return to the previous menu

        response = launch_smart_contract_template(contract_type)
        print(response)

if __name__ == "__main__":
    main()

