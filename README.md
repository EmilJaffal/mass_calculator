# Mass Calculator Application

This project is a mass calculator application that allows users to calculate the masses of elements in chemical formulas. It provides a command-line interface for user interaction and supports batch processing of formulas from various input sources.

## Project Structure

```
mass_calculator
├── src
│   ├── main.py                # Main logic of the mass calculator application
│   ├── util
│   │   ├── __init__.py        # Initialization file for the util package
│   │   └── batch_processing.py  # Utility functions for batch processing of formulas
├── requirements.txt            # Python dependencies required for the project
├── runtime.txt                 # Python runtime version for Heroku
├── Procfile                    # Commands executed by the Heroku app on startup
└── README.md                   # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mass_calculator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the correct Python version specified in `runtime.txt`.

## Usage

To run the mass calculator application, execute the following command:

```
python src/main.py
```

Follow the prompts to enter chemical formulas and calculate element masses.

## Batch Processing

The application supports batch processing of chemical formulas from text files and Excel files. You can use the utility functions in `src/util/batch_processing.py` to read formulas from different input sources.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.