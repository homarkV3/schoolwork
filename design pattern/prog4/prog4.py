from command_processor import CommandProcessor

if __name__ == "__main__":
    command_file = "commands.txt"  # Adjust the file path as needed
    processor = CommandProcessor(command_file)
    processor.process_commands()
