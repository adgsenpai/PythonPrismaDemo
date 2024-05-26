# Python Prisma Demo

This is a demo project that uses Prisma to interact with a PostgreSQL database in a Python application. The project demonstrates how to create, retrieve, and list users from a PostgreSQL database using Prisma and asyncio.

## Prerequisites

- Python 3.7 or later
- PostgreSQL database
- Node.js and npm

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/adgsenpai/pythonprismademo.git
cd pythonprismademo
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install prisma
```

### 3. Configure the Database

Ensure you have a PostgreSQL database set up. Create a `.env` file in the project root with your database connection URL:

```plaintext
DATABASE_URL="postgresql://animeflixusr:your_password@vm.adgstudios.co.za:5432/demodb?schema=public"
```

### 4. Set Up Prisma

#### Initialize Prisma and Generate Client

First, install Prisma CLI globally if you haven't already:

```bash
npm install -g prisma
```

Then, run the following commands to initialize Prisma and generate the Prisma client:

```bash
prisma init
prisma generate
```

### 5. Create the Database Schema

Ensure your `schema.prisma` file includes the following:

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator db {
  provider             = "prisma-client-py"
  interface            = "asyncio"
  recursive_type_depth = 5
}

model Users {
  id        String   @id
  email     String   @unique
  password  String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

### 6. Push the Schema to the Database

Run the following command to push your Prisma schema to your PostgreSQL database:

```bash
prisma db push
```

## Usage

Run the Python script to create, retrieve, and list users:

```bash
python demo.py
```
 

## Example Python Script

Here is an example of a Python script (`main.py`) that interacts with the PostgreSQL database using Prisma:

```python
import asyncio
from prisma import Prisma

# Define the main async function
async def main() -> None:
    # Instantiate the Prisma client
    db = Prisma()

    # Connect to the database
    await db.connect()

    # Create a new user in the database
    user = await db.users.create(
        {
            'id': '1',
            'email': 'user@example.com',
            'password': 'securepassword',
        }
    )
    print(f'Created user: {user.json(indent=2, sort_keys=True)}')

    # Find the user by their unique ID
    found = await db.users.find_unique(where={'id': user.id})
    assert found is not None
    print(f'Found user: {found.json(indent=2, sort_keys=True)}')

    # Select and print all users from the database
    all_users = await db.users.find_many()
    print('All users:')
    for user in all_users:
        print(user.json(indent=2, sort_keys=True))

    # Disconnect from the database
    await db.disconnect()

# Run the main async function
if __name__ == '__main__':
    asyncio.run(main())
```

 