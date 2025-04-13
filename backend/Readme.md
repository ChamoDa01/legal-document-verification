# Install PostgreSQL if not already installed
# On Ubuntu: sudo apt install postgresql postgresql-contrib
# On macOS with Homebrew: brew install postgresql

sudo apt install libpq-dev

# Create a database for our application
sudo -u postgres createdb legaldocdb

# Create a user with password
sudo -u postgres psql -c "CREATE USER docadmin WITH PASSWORD 'your_password';"

# Grant privileges to the user
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE legaldocdb TO docadmin;"