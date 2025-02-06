# Streamlit Multi-Page with Authentication

This project provides a template for a multi-page Streamlit application with built-in user authentication. It includes examples of how to handle user login, registration, and secure session management.

## Features

- Multi-page application structure
- User authentication (login, registration)
- Secure session management
- Configurable settings via `config.yaml` file

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or later
- `pip` (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/b-macd/streamlit-multi-page-with-authentication.git
   cd streamlit-multi-page-with-authentication
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Before running the application, you need to configure the settings. Create a `secrets.toml` file in the hidden `.streamlit` directory and specify the path to the `config.yaml` file as follows:

```
config_file_path = path/to/config/file
```

Replace `path/to/config/file` with the actual path to your `config.yaml` file.

### Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

The application should now be accessible at `http://localhost:8501`.

## Usage

- Navigate through the different pages using the sidebar.
- Register a new account or log in with an existing account to access secured pages.
- Use the `config.yaml` file to customize the application settings.

## Folder Structure

```
streamlit-multi-page-with-authentication/
├── .streamlit/
│   └── secrets.toml
├── pages/
│   ├── Page1.py
│   ├── Page2.py
│   └── ...
├── app.py
├── config.yaml
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Streamlit for providing an amazing framework.
- The open-source community for their invaluable contributions.
