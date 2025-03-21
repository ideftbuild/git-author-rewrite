# git-author-rewrite

A simple command-line tool to update author information in your Git commit history.

## Why this tool?

Ever needed to update your commit history because:
- You forgot to set your Git email correctly
- Your company changed email domains
- You want to sync personal and work commits

`git-author-rewrite` helps you fix these issues without affecting other contributors' work.

## Features

- Update author name and email in commit history
- Preserve commit dates and messages
- Keep other contributors' commits unchanged
- Simple command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/ideftbuild/git-author-rewrite
```

## Quick Start

```bash
# Basic usage
git-author-rewrite --email <old-email> <new-email>

# Update both name and email
git-author-rewrite --email <old-email> <new-email> --name <old-name> <new-name>
```

## Usage Guide

To rewrite only the email address, run the following command:

```bash
git-author-rewrite --email <old-email> <new-email>
```

To rewrite only the author name, use this command:

```bash
git-author-rewrite --name <old-name> <new-name>
```

To rewrite both the email address and the author name, use the command below:

```bash
git-author-rewrite --email <old-email> <new-email> --name <old-name> <new-name>
```

## Common Use Cases

1. Updating work email
   ```bash
   git-author-rewrite --email "name@oldcompany.com" "name@newcompany.com"
   ```

2. Fixing misconfigured author
   ```bash
    git-author-rewrite --email "name@oldcompany.com" "name@newcompany.com" --name "old name" "new name"
   ```

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/git-author-rewrite.git
    cd git-author-rewrite
    ```

2. Install the project dependencies using Poetry

    ```bash
    poetry install
    ```

3. Run tests to verify everything is set up correctly:

    ```bash
    poetry run pytest
    ```

4. Run the command 
    ```bash
    poetry run git-author-rewrite
    ```

## Important Notes

- Always backup your repository before running the tool
- Test on a small set of commits first
- Push changes to remote with `--force` after running the tool


## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


## Credits

Created by Akaniyene Effiong

## 📢 Support

Found a bug or need help? [Open an issue](https://github.com/ideftbuiuld/git-author-rewrite/issues)
