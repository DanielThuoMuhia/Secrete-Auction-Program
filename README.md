# Bidding Application

This Python application allows users to participate in a bidding process. It collects bids from multiple participants and determines the highest bidder once the bidding process is complete.

## Features

- **Bid Collection**: Allows multiple participants to place bids.
- **Clear Console**: Clears the console between new bids for better readability.
- **Determine Winner**: Identifies and displays the highest bidder.

## Project Structure

- **`main.py`**: The main script that handles the bidding process, including collecting bids, validating input, and determining the highest bidder.
- **`art.py`**: Contains the `logo` used in the application (assumed to be a text-based art logo).

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/DanielThuoMuhia/Secrete-Auction-Program.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd YourRepositoryName
    ```

3. **Ensure Dependencies**:
   - This project does not require any external dependencies beyond the standard Python library.

## Usage

1. **Run the Program**:

    ```bash
    python main.py
    ```

2. **Participate in Bidding**:
   - Enter your name and bid amount when prompted.
   - After submitting your bid, you will be asked if there are any other bidders.
   - Type `yes` if there are more bidders or `no` to end the bidding process and determine the winner.

3. **Example Interaction**:

    ```plaintext
    What is your name?: Alice
    What is your bid?: $150
    Are there any other bidders? Type 'yes' or 'no'.
    ```

    If `no` is entered, the program will display:

    ```plaintext
    The winner is Alice with a bid of $150
    ```

## Code Overview

- **`main.py`**:
  - **`print(logo)`**: Displays the logo at the start of the program.
  - **`bids` dictionary**: Stores the names and bid amounts of participants.
  - **`find_highest_bidder` function**: Determines and prints the highest bidder.
  - **Bidding loop**: Handles user input for bids and manages the bidding process.

- **`art.py`**:
  - **`logo`**: Contains the ASCII art logo displayed at the start of the application.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or make a pull request. Ensure that your contributions adhere to the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [daniel.thuo@students.jkuat.ac.ke](mailto:daniel.thuo@students.jkuat.ac.ke).

Happy bidding!
